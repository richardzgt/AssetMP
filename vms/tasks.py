# -*- coding: utf-8 -*-
# @Author: gaotao
# @Date:   2018-04-25 21:38:24
# @Last Modified by:   gaotao
# @Last Modified time: 2018-05-11 14:35:51
# Purpose: 
# 


# from celery import task
from pysphere import VITask,VIServer,resources
# from AssetMP.settings import *
# from AssetMP.api import logger
import logging
from multiprocessing import Process
import ssl
import os
import time
ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                format='%(levelname)s [%(asctime)s] [%(pathname)s L%(lineno)d] %(message)s')


class VMHandler(object):
    """通过vc api处理vm"""
    def __init__(self, vm_name):
        super(VMHandler, self).__init__()
        self.vm_name = vm_name
        try:
            self.server = VIServer()
            self.server.connect('vcenter.config.net','administrator@vcenter.config.net','huoRED8818!!')

        except Exception as e:
            logger.error(e)


    def _clone_vm(self, template_name):
        """
        parameter: 
            appname: cif-base-98-1
            static_params: ，模板名称规则
            hostname: 
        过程日志
        结果  提交到数据库
        """
        try:
            logger.info( "subprocess get pid: %s" % os.getpid())
            template_vmx = self.server.get_vm_by_name(template_name, datacenter="Datacenter")

            # sync_run=True返回一个vm对象，反之是一个task对象
            clone_vm = template_vmx.clone(self.vm_name,sync_run=True)
            while True:
                try:
                    clone_vm.login_in_guest('root','huored')
                    pid = clone_vm.start_process('/usr/bin/curl',args=["http://yumos.ops.net/script/install-dev.sh","-o","/tmp/install-dev.sh"],cwd='/root')
                    logger.debug("Get script,pid:[%s]" % pid)
                    clone_vm.list_files('/tmp/install-dev.sh')
                    pid = clone_vm.start_process('/bin/bash',args=["/tmp/install-dev.sh",self.vm_name],cwd='/root')
                    logger.info("Run script,pid:[%s]" % pid)
                    logger.info("Complete !!!")
                    break
                except resources.vi_exception.VIApiException:
                    logger.debug("FileNotFoundFault")
                    continue
                except Exception as e:
                    logger.warn(e)
                    time.sleep(10)
                    if clone_vm.is_powered_off():
                        clone_vm.is_powered_on()
            # 把这个成功的虚拟机实例记录到数据库
            # print VITask.get_result(task_id)
        except Exception as e:
            logger.error(e)

       
    def clone_vm(self, template_name):
            # 检查是否已存在
            # 组装参数
            # 直接执行，不等待
            ### 启动日志，插入数据库
            if self.exist_vm_check():
                logger.info("vm: [%s] exist" % self.vm_name) 
            else:
                try:
                    p = Process(target=self._clone_vm,args=(template_name,))
                    p.start()
                except Exception as e:
                    logger.info("run error")
                    logger.error(e)


    def exist_vm_check(self):
        try:
            self.server.get_vm_by_name(self.vm_name)
            return True
        except resources.vi_exception.VIException:
            logger.debug("Could not find a VM named %s" % self.vm_name)
        
        return False


# v = VMHandler('cif.base-98-14')
# v.clone_vm()