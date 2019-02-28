# -*- coding: utf-8 -*-
# @Author: richard
# @Date:   2018-04-10 19:13:25
# @Last Modified by:   richardzgt﻿​
# @Last Modified time: 2018-10-12 10:34:08
# Purpose: 
# 
from django.db import models
from django.forms import ModelForm
from django.db.models import Count,F
from django.db.models.query import QuerySet,Q
from django.utils.html import format_html
import pytz,datetime


class ManType(models.Model):
    name = models.CharField(max_length=32)
    detail = models.CharField(max_length=32, blank=True, null=True)
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    class Meta:
        verbose_name = verbose_name_plural = u"厂家信息"
    def __unicode__(self):
        return self.name

class AssetStatus(models.Model):
    name = models.CharField(max_length=32)
    detail = models.CharField(max_length=32, blank=True, null=True)
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    class Meta:
        verbose_name = verbose_name_plural = u"设备状态"
    def __unicode__(self):
        return self.name

class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'机房名称')
    bandwidth = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'机房带宽')
    linkman = models.CharField(max_length=16, blank=True, null=True, default='', verbose_name=u'联系人')
    phone = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'联系电话')
    address = models.CharField(max_length=128, blank=True, null=True, default='', verbose_name=u"机房地址")
    network = models.TextField(blank=True, null=True, default='', verbose_name=u"IP地址段")
    date_added = models.DateField(auto_now=True, null=True)
    operator = models.CharField(max_length=32, blank=True, default='', null=True, verbose_name=u"运营商")
    comment = models.CharField(max_length=128, blank=True, default='', null=True, verbose_name=u"备注")
    needed_cabinet = models.BooleanField(default=True,verbose_name=u"是否需要渲染机架图")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u"IDC机房"


class Platform(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'平台名称')
    nickname = models.CharField(max_length=32, verbose_name=u'平台简称')
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u"平台信息"
            
class Belong(models.Model):
    """所属公司"""
    name = models.CharField(max_length=32, verbose_name=u'公司名称')
    nickname = models.CharField(max_length=32, verbose_name=u'平台简称')
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u"所属公司"
        

class SignDep(models.Model):
    """维保单位"""
    name = models.CharField(max_length=32, verbose_name=u'维保公司名称')
    contact = models.CharField(max_length=32, verbose_name=u'联系人')
    phone = models.CharField(max_length=32, verbose_name=u'联系方式')
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u"维保单位"
        
class Usage(models.Model):
    """
    设备使用类型： 数据库 物理机系统 虚拟机节点 容器主机节点
    """
    name = models.CharField(max_length=60)
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')

class Asset(models.Model):
    """
    设备信息表
    """
    MachineType_CHOICE = (
        (0, u'防火墙'),
        (1, u'路由器'),
        (2, u'交换机'),
        (3, u'物理机'),
    )

    UHIGH_CHOICE = (
        (0, 1),
        (1, 2),
        (2, 4)
    )

    hostname = models.CharField(max_length=50,blank=True, null=True)
    machine_type = models.IntegerField(choices=MachineType_CHOICE, verbose_name=u"设备类型")
    usage = models.ForeignKey(Usage, blank=True, null=True, verbose_name=u"主机使用类型")
    ipadd = models.CharField(max_length=20,blank=True, null=True)
    manager_ip = models.CharField(max_length=20,blank=True, null=True, verbose_name=u'管理网ip')
    remote_card_ip = models.CharField(max_length=20,blank=True, null=True,verbose_name=u'远控卡ip')
    manufacturer = models.ForeignKey(ManType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"厂家")
    product_name = models.CharField(max_length=20,verbose_name=u'设备型号')
    serial_number = models.CharField(max_length=20,unique=True,verbose_name=u'序列号')
    suppliers = models.CharField(max_length=32,blank=True, null=True, verbose_name=u'供应商')
    purchase_at = models.DateField(auto_now=True, auto_now_add=False,verbose_name=u'购买时间')
    department = models.CharField(max_length=20,blank=True, null=True,verbose_name=u'使用部门')
    idc = models.ForeignKey(IDC, on_delete=models.DO_NOTHING, verbose_name=u'机房')
    platform =  models.ForeignKey(Platform, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'平台名称')
    sign_dep =  models.ForeignKey(SignDep, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'维保单位')
    sign_time = models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name=u'维保签约时间')
    expire_time = models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True,verbose_name=u'维保过期时间')
    belong =  models.ForeignKey(Belong, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'所属公司')
    cpu = models.CharField(max_length=60,blank=True, null=True)
    disk = models.CharField(max_length=60,blank=True, null=True)
    memory = models.CharField(max_length=60,blank=True, null=True)
    system_version = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"操作系统")
    cabinet = models.CharField(max_length=32, verbose_name=u'机柜号')
    uhight = models.IntegerField(choices=UHIGH_CHOICE, default=UHIGH_CHOICE[0][0]  ,verbose_name=u"u高")
    railnum = models.IntegerField(verbose_name=u"导轨位置")
    number = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资产编号')
    status = models.ForeignKey(AssetStatus, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"机器状态")
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    
    def __unicode__(self):
        return self.hostname


    def expire_time_status(self):
        # try:
        if self.expire_time:
            now = datetime.date.today()
            off_guarantee = now > self.expire_time 
            display_time = self.expire_time.strftime('%Y-%m-%d')
            if off_guarantee:
                color_code = 'red'
            else:
                color_code = 'green'
            return format_html('<span style="color: {};">{}</span>',
                    color_code,
                    display_time)
        # except Exception as e :
            # return "[ERR] %s" % str(e)

    expire_time_status.short_description = u"过保时间"

    class Meta:
        verbose_name = verbose_name_plural = u"设备信息表"



class AssetRecord(models.Model):
    """
    记录设备工单和变动
    """
    asset = models.ForeignKey(Asset)
    username = models.CharField(max_length=30, null=True)
    alert_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

def group_by(query_set, group_by):
    '''util:django 获取分类列表'''
    assert isinstance(query_set, QuerySet)
    django_groups = query_set.values(group_by).annotate(Count(group_by))
    groups = []
    for dict_ in django_groups:
        groups.append(dict_.get(group_by))
    return groups

