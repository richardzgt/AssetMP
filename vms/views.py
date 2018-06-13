# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404,QueryDict

from django.views.generic import View,TemplateView, ListView, RedirectView, FormView
from vms.tasks import VMHandler
from vms.models import Vms

class VmsCreate(View):
    """
    调用vc接口，创建虚拟机
    :param request:
    :return:
    """
    # asset = get_object_or_404(Asset, id=asset_id)
    def get(self, request):
        try:
            
            # 检查是否已存在
            # 组装参数
            # 直接执行，不等待
            ### 启动日志，插入数据库
            # p = Process(target=clone_vm)
            # p.start()
            # if r == 'running':
                # insert db set state 1
            vm = VMHandler('cif.base-98-14')
            ret =  vm.exist_vm_check()
            vm.clone_vm()
            return HttpResponse(ret)
        except Exception as e:
            return HttpResponse('error....... %s' % e)
        return render(request,'assets/cabinet.html', locals())


    def post(self, request):
        pass


