#!/user/bin/env python
#coding=utf8
import json

import pymongo




class MongoDatabaseContext():

    def __init__(self, host, user, password, auth_database,database, port=27017):
        """初始化数据"""
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.auth_database = auth_database
        self.database = database

    def __enter__(self):
        """数据库连接，并返回cursor """
        self.client = pymongo.MongoClient(self.host, self.port)
        # 获得数据库的权限
        self.client[self.auth_database].authenticate(self.user, self.password, mechanism="SCRAM-SHA-1")
        control_database = self.client.get_database(name=self.database)
        return control_database

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭数据库连接"""
        self.client.close()
        print "__exit__ zhixingla"
        #return True