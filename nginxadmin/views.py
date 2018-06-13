from django.shortcuts import render

# Create your views here.



from django.shortcuts import get_object_or_404,render_to_response,HttpResponseRedirect,render
from django.http import JsonResponse, HttpResponse, Http404,QueryDict
from django.template import RequestContext
from django.views.generic import View,TemplateView, ListView, RedirectView, FormView

# from settings import *
import json
import commands


class NginxTree(View):
    """docstring for NginxTree"""
    def get(self):
        jsonlist = []
        f_id=1
        for file in os.listdir(config.nginx_conf_path):
            jsonlist.append({"id": f_id, "pId": 0, "name": file})
            # f_id=f_id+1
            config_file = config.nginx_conf_path+file
            if not all((os.path.isfile(config_file),config_file.endswith('.conf'))): continue
            c = nginx.loadf(config.nginx_conf_path+file)
            Upstreams = c.filter(btype="Upstream")
            u_id = 0
            s_id = 0
            all_upstreams = [ x.value for x in Upstreams ]
            if len(all_upstreams) > 0: 
                jsonlist.append({"id": int(str(f_id)+"2"), "pId": f_id, "name": "upstream"})

            jsonlist.append({"id": int(str(f_id)+"3"), "pId": f_id, "name": "servers"})

            
            for i in Upstreams:
                id = int(str(f_id)+"2" + str(u_id + 1))
                jsondict = {"id": id, "pId": int(str(f_id)+"2"), "name": i.value}
                u_id = u_id + 1
                # print type(u_id),u_id
                jsonlist.append(jsondict)
            Servers = c.filter(btype="Server", name='')
            for i in Servers:
                server_name = i.filter("key", "server_name")[0].value
                id = int(str(f_id)+"3" + str(s_id + 1))
                jsondict = {"id": id, "pId": int(str(f_id)+"3"), "name": server_name}
                s_id = s_id + 1
                # print type(s_id),s_id
                jsonlist.append(jsondict)
            f_id = f_id + 1