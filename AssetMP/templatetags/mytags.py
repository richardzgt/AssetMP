# -*- coding: utf-8 -*-
# @Author: richard
# @Date:   2018-04-16 17:11:50
# @Last Modified by:   高涛
# @Last Modified time: 2018-04-18 10:26:40
# Purpose: 
# 


from django import template
import re
import ast
import time


register = template.Library()


@register.filter(name='str_to_list')
def str_to_list(info):
    """
    str to list
    """
    # print ast.literal_eval(info), type(ast.literal_eval(info))
    return ast.literal_eval(info)


@register.filter(name='int2str')
def int2str(value):
    """
    int 转换为 str
    """
    return str(value)
