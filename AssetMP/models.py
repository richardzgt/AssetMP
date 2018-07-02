# -*- coding: utf-8 -*-
# @Author: richard
# @Date:   2018-04-10 19:13:25
# @Last Modified by:   richardzgt﻿​
# @Last Modified time: 2018-07-02 16:09:27
# Purpose: 
# 
from django.db import models
from django.forms import ModelForm
from django.db.models import Count,F
from django.db.models.query import QuerySet,Q


# MACHINE_TYPE = (
#     (1, U'物理机'),
#     (2, U'防火墙'),
#     (3, U'交换机'),
#     (4, U'路由器'),
#     (5, U'数据库'),
#     (6, U'其他'),
#     )

# MAN_TYPE = (
#     (1, U'DELL'),
#     (2, U'易星'),
#     (3, U'沃趣'),
#     (4, U'H3C'),
#     (5, U'金盾'),
#     )

# AREA_TYPE = (
#     (1, U'兴议'),
#     (2, U'三墩'),
#     (3, U'嘉兴'),
#     (4, U'金华'),
#     (5, U'西溪'),
#     )

# ASSET_STATUS = (
#     (1, u"已使用"),
#     (2, u"未使用"),
#     (3, u"报废")
#     )


class MachineType(models.Model):
    name = models.CharField(max_length=32)
    detail = models.CharField(max_length=32, blank=True, null=True)
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    class Meta:
        verbose_name = u"主机使用类型"
    def __unicode__(self):
        return self.name

class ManType(models.Model):
    name = models.CharField(max_length=32)
    detail = models.CharField(max_length=32, blank=True, null=True)
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    class Meta:
        verbose_name = u"厂家信息"
    def __unicode__(self):
        return self.name

class AssetStatus(models.Model):
    name = models.CharField(max_length=32)
    detail = models.CharField(max_length=32, blank=True, null=True)
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    class Meta:
        verbose_name = u"设备状态"
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
        verbose_name = u"IDC机房"


class Platform(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'平台名称')
    nickname = models.CharField(max_length=32, verbose_name=u'平台简称')
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"平台信息"
            
class Belong(models.Model):
    """所属公司"""
    name = models.CharField(max_length=32, verbose_name=u'公司名称')
    nickname = models.CharField(max_length=32, verbose_name=u'平台简称')
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"所属公司"
        

class Asset(models.Model):
    """
    设备信息表
    """
    machine_type = models.ForeignKey(MachineType, on_delete=models.DO_NOTHING, verbose_name=u"设备类型")
    hostname = models.CharField(max_length=50,blank=True, null=True)
    ipadd = models.CharField(max_length=20,blank=True, null=True)
    manager_ip = models.CharField(max_length=20,blank=True, null=True, verbose_name=u'管理网ip')
    remote_card_ip = models.CharField(max_length=20,blank=True, null=True,verbose_name=u'远控卡ip')
    manufacturer = models.ForeignKey(ManType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"厂家")
    product_name = models.CharField(max_length=20,verbose_name=u'设备型号')
    serial_number = models.CharField(max_length=20,unique=True,verbose_name=u'序列号')
    suppliers = models.CharField(max_length=32,blank=True, null=True, verbose_name=u'供应商')
    sign_time = models.CharField(max_length=20,blank=True, null=True,verbose_name=u'签约时间')
    expire_time = models.CharField(max_length=20,blank=True, null=True,verbose_name=u'过期时间')
    department = models.CharField(max_length=20,blank=True, null=True,verbose_name=u'使用部门')
    idc = models.ForeignKey(IDC, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'机房')
    platform =  models.ForeignKey(Platform, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'平台名称')
    sign_dep = models.CharField(max_length=20,blank=True, null=True,verbose_name=u"维保单位")
    belong =  models.ForeignKey(Belong, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'所属公司')
    cpu = models.CharField(max_length=60,blank=True, null=True)
    disk = models.CharField(max_length=60,blank=True, null=True)
    memory = models.CharField(max_length=60,blank=True, null=True)
    system_version = models.CharField(max_length=80, blank=True, null=True, verbose_name=u"操作系统")
    cabinet = models.CharField(max_length=32, verbose_name=u'机柜号')
    uhight = models.IntegerField(verbose_name=u"u高")
    railnum = models.IntegerField(verbose_name=u"导轨位置")
    number = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资产编号')
    status = models.ForeignKey(AssetStatus, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"机器状态")
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'备注')
    
    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = u"设备信息表"

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

