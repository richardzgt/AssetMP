# -*- coding: utf-8 -*-
# @Author: richard
# @Date:   2018-04-10 18:28:30
# @Last Modified by:   gaotao
# @Last Modified time: 2018-05-21 13:04:25
# Purpose: 
# 


from django.shortcuts import get_object_or_404,render_to_response,HttpResponseRedirect,render
from django.http import JsonResponse, HttpResponse, Http404,QueryDict
from django.template import RequestContext
from AssetMP.models import *
from django.db.models import Q
from AssetMP.api import get_rack_rail_template,logger,json_returner,pages
from django.views.generic import View,TemplateView, ListView, RedirectView, FormView
from django.contrib.admin.models import LogEntry,ADDITION,DELETION,CHANGE,ContentType

class Assets(View):
    def get(self, request):
        server_id = request.GET.get('id','')
        keyword = request.GET.get('keyword','')
        if server_id:
            assets = Asset.objects.filter(id=server_id)
        elif keyword:
            assets = Asset.objects.filter(
                Q(hostname__icontains=keyword) |
                Q(ipadd__contains=keyword) |
                Q(manager_ip__contains=keyword) |
                Q(remote_card_ip__contains=keyword) |
                Q(product_name__icontains=keyword) |
                Q(serial_number__icontains=keyword) |
                Q(suppliers__contains=keyword) |
                Q(expire_time__contains=keyword) |
                Q(idc__name__contains=keyword) |
                Q(manufacturer__name__icontains=keyword) |
                Q(machine_type__name__contains=keyword) |
                Q(platform__name__contains=keyword) |
                Q(cpu__contains=keyword) |
                Q(disk__contains=keyword) |
                Q(memory__contains=keyword) |
                Q(cabinet__contains=keyword) |
                Q(status__name__contains=keyword) |
                Q(describe__contains=keyword) |
                Q(system_version__contains=keyword))
        else:
            assets = Asset.objects.all()
        # return render_to_response('assets/index.html', locals(),context_instance=RequestContext(request))

        assets_list, p, assets, page_range, current_page, show_first, show_end = pages(assets, request)

        return render(request,'assets/index.html', locals())

class AssetDetail(View):
    """docstring for AssetDetail"""
    def get(self, request):
        try:
            server_id = request.GET.get('id','')
            asset = Asset.objects.get(id=server_id)
            _all_asset_logs = LogEntry.objects.filter(content_type=ContentType.objects.get(model='Asset'))
            asset_logs = _all_asset_logs.filter(object_id=server_id)
            # for log in asset_logs:
                # setattr(log, )
            for log in asset_logs:
                log_dict = {} 
                if log.action_flag == ADDITION: flag = "新增"
                if log.action_flag == DELETION: flag = "删除"
                if log.action_flag == CHANGE: flag = "修改"
                setattr(log, 'action_flag', flag)
        except Exception as e:
            return HttpResponse('error')
        return render(request,'assets/detail.html', locals())
        

class Cabinet(View):
    """
    利用插件获取 机架图
    :param request:
    :param asset_id:
    :return:
    """
    # asset = get_object_or_404(Asset, id=asset_id)
    def get(self, request):
        server_id = request.GET.get('id','')
        idc_id = request.GET.get('idc_id','')
        keyword = request.GET.get('keyword','')
        assets = ''
        idc = ''
        if server_id:
            server = Asset.objects.filter(id=server_id)
            return json_returner(server)

        _idc_all = set([ i.idc for i in Asset.objects.all() ])
        idc_all = list(_idc_all)
        if idc_id:
            idc = IDC.objects.get(id=idc_id)

            if keyword :
                assets = Asset.objects.filter(
                    Q(hostname__icontains=keyword) |
                    Q(ipadd__contains=keyword) |
                    Q(manager_ip__contains=keyword) |
                    Q(remote_card_ip__contains=keyword) |
                    Q(product_name__icontains=keyword) |
                    Q(serial_number__icontains=keyword) |
                    Q(suppliers__contains=keyword) |
                    Q(expire_time__contains=keyword) |
                    Q(idc__name__contains=keyword) |
                    Q(manufacturer__name__icontains=keyword) |
                    Q(machine_type__name__contains=keyword) |
                    Q(platform__name__contains=keyword) |
                    Q(cpu__contains=keyword) |
                    Q(disk__contains=keyword) |
                    Q(memory__contains=keyword) |
                    Q(cabinet__contains=keyword) |
                    Q(status__name__contains=keyword) |
                    Q(describe__contains=keyword) |
                    Q(system_version__contains=keyword)).filter(idc=idc_id)

            # assets = assets.filter(idc=idc_id)
            rack_rail_template = get_rack_rail_template(idc,assets)

        return render(request,'assets/cabinet.html', locals())

class getCorp(View):
    """docstring for getCorp"""
    def get(self, request):
        try:
            corp_id = request.GET.get('corp_id','')
            corp = Belong.objects.filter(id=corp_id)
            return json_returner(corp)
        except Exception as e:
            return "faild"
        

def dashboard(request):
    pass
    return render_to_response('assets/dashboard.html', locals(),context_instance=RequestContext(request))


