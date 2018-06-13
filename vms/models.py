# -*- coding: utf-8 -*-
# @Author: gaotao
# @Date:   2018-04-26 11:09:12
# @Last Modified by:   gaotao
# @Last Modified time: 2018-05-03 18:14:40
# Purpose: 
# 



from django.db import models
from django.forms import ModelForm
from django.db.models import Count,F
from django.db.models.query import QuerySet,Q
from django.contrib.auth.models import User



STATUS = (
    (1, U'已提交vc成功'),
    (2, U'已提交vc失败'),
    (3, U'任务执行完成'),
    (4, U'任务执行失败'),
    )

NOTICE = (
    (1, U'已阅读'),
    (2, U'未阅读'),
    (3, U'已推送'),
    (4, U'未推送'),
    )


class Template(models.Model):
    """模板 Template 在哪里vm就在哪里生成"""
    name = models.CharField(max_length=32, verbose_name=u'模板名称(VC)')
    host = models.CharField(max_length=32, verbose_name=u'所在主机')
    describe = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'模板描述')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"模板"

class Vms(models.Model):
    """
    虚拟机创建
    
    """
    owner = models.ForeignKey(User, verbose_name=u"提交用户")
    status = models.IntegerField(choices=STATUS, verbose_name=u"虚拟机创建状态")
    vmname = models.CharField(max_length=100, verbose_name=u'创建主机名')
    create_at = models.DateField(auto_now=True, null=True,  verbose_name=u'创建时间')
    finish_at = models.DateField(auto_now=True, null=True,  verbose_name=u'完成时间')
    template = models.ForeignKey(Template, verbose_name=u"模板") 
    notice = models.IntegerField(choices=STATUS,verbose_name=u'通知状态')
    result = models.TextField(null=True, blank=True, verbose_name=u'执行结果日志')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")
    
