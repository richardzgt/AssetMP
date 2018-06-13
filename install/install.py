# -*- coding: utf-8 -*-
# @Author: gaotao
# @Date:   2018-05-21 10:32:29
# @Last Modified by:   gaotao
# @Last Modified time: 2018-05-21 10:43:15

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AssetMP.settings")

import django
from AssetMP.models import Platform,Asset,IDC,AssetStatus,ManType,MachineType

if django.VERSION >= (1, 7): 
    django.setup()


MachineType.objects.create(name=u'物理机')
MachineType.objects.create(name=u'防火墙')
MachineType.objects.create(name=u'交换机')
MachineType.objects.create(name=u'路由器')
MachineType.objects.create(name=u'数据库')


