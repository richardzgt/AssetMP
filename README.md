本项目的目的是建立一个资管平台，用于直观管理机柜和服务器资源。

1 使用方法：
   安装必要的包
   pip insatll -r install/requirements.txt
   
   创建数据库和用户
   create database amp default charset 'UTF8';

   编辑Asset/setting.py，把数据库信息填到DATABASE

   创建数据
   python manager.py syncdb 或者 migrate


2 使用django后台admin管理：
   编辑主机使用类型s（machine_type）中添加设备类型，注意 物理机和数据库类型是必填的，也是通过这个来渲染模板

3 assets批量导入：
  执行：python install/import.py
  字段格式请看 install/asset.csv          

4 启动 
nohup python manage.py  runserver 0.0.0.0:8080 &


5 更新:
  增加维保供应商
  将admin管理中,资产过维保日期的标红
  

![p1](https://github.com/richardzgt/AssetMP/blob/master/install/pic/20180614095254.png)
![p2](https://github.com/richardzgt/AssetMP/blob/master/install/pic/20180614095520.png)
![p3](https://github.com/richardzgt/AssetMP/blob/master/install/pic/20180614095600.png)
![p4](https://github.com/richardzgt/AssetMP/blob/master/install/pic/20180614095649.png)