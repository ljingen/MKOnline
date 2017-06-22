# -*- encoding:utf-8 -*-
import pymysql
# 由于Django内部连接MySQL时使用的是MySQLdb模块，而python3中还无此模块，所以需要使用pymysql来代替
# 如下设置放置的与project同名的配置的 __init__.py文件中
pymysql.install_as_MySQLdb()