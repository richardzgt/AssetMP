# -*- coding: utf-8 -*-
# @Author: gaotao
# @Date:   2018-05-22 16:06:44
# @Last Modified by:   gaotao
# @Last Modified time: 2018-05-22 16:10:51
# Purpose: 
# 


from django.conf.urls import patterns, include, url
from django.contrib import admin
from nginxadmin.views import *


urlpatterns = patterns('nginxadmin.views',
            url(r'^nginx_tree', NginxTree.as_view(), name='nginx_tree'),
            )

