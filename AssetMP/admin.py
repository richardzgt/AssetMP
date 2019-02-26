# -*- coding: utf-8 -*-
# @Author: richard
# @Date:   2018-04-12 15:39:37
# @Last Modified by:   richardzgt﻿​
# @Last Modified time: 2018-11-29 15:54:06
# Purpose: 


from django.contrib import admin
from models import *
from django.contrib.admin.models import LogEntry
import json


admin.site.site_header = 'AMP资产管理系统'  # 此处设置页面显示标题
admin.site.site_title = 'AMP资产管理系统'  # 此处设置页面头部标题
        

class AssetMPAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Asset._meta.fields ]
    list_display.remove('id')
    list_display.remove('expire_time')
    list_display.insert(15,'expire_time_status')  # 第15个槽位插入
    # list_display = ('hostname','idc','ipadd','serial_number')
    list_filter = ('machine_type','idc','product_name','manufacturer')
    search_fields = ['serial_number']

class IDCAdmin(admin.ModelAdmin):
    list_display = ('name','comment')
    # def log_change(self, request, object, message):
    """
    <QueryDict: {u'comment': [u'67788'], u'name': [u'\u5174\u8bae'], u'_save': [u'Save'], u'linkman': [u''], u'phone': [u''], u'bandwidth': [u'50'], u'address': [u''], u'operator': [u''], u'csrfmiddlewaretoken': [u'a44q3q6NYHtkS4RJGrwGiVM6rF5v12Fk'], u'network': [u'']}> ================ {'comment': u'67788', 'name': u'\u5174\u8bae', 'linkman': u'', '_state': <django.db.models.base.ModelState object at 0x7f111c37a590>, 'phone': u'', 'bandwidth': u'50', 'address': u'', 'operator': u'', 'date_added': datetime.date(2018, 4, 17), 'id': 2L, 'network': u''}
    request 和 object 竟然是一样的
    """
    #     # print request.POST.__dict__, object,message  
    #     _message = recodeDiff(request, object)
    #     newmessage = json.dumps(_message,encoding='utf-8',ensure_ascii=False)
    #     super(IDCAdmin, self).log_change(request, object, newmessage)  

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name','describe')

class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ('name','describe')

class ManTypeAdmin(admin.ModelAdmin):
    list_display = ('name','describe')

class AssetStatusAdmin(admin.ModelAdmin):
    list_display = ('name','describe')

class BelongAdmin(admin.ModelAdmin):
    list_display = ('name','nickname','describe')

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user','content_type',)

class SignDepAdmin(admin.ModelAdmin):
    list_display = ('name','contact','phone','describe')
        


admin.site.register(Asset,AssetMPAdmin)
admin.site.register(IDC,IDCAdmin)
admin.site.register(Platform,PlatformAdmin)
admin.site.register(MachineType,MachineTypeAdmin)
admin.site.register(ManType,ManTypeAdmin)
admin.site.register(AssetStatus,AssetStatusAdmin)
admin.site.register(LogEntry,LogEntryAdmin)
admin.site.register(Belong, BelongAdmin)
admin.site.register(SignDep, SignDepAdmin)



def recodeDiff(request, object):
    alert_dict = []
    old_dict = object.__dict__
    for field, new in request.POST.items():
        old = old_dict.get(field)
        print old,new,"======"
        if unicode(old) != unicode(new) and not field.startswith('_'):
            alert_dict.append(u"change field {2}: {1} to {0}".format(old,new,field))
    return alert_dict

