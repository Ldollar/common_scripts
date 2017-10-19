#!usr/bin/env python
# -*- coding:utf-8 -*-
# 作用登录连接SFTP，并进行查找，上传，下载等操作，当无法连接时，显示错误代码
import json
import sys

import logging
import paramiko as paramiko

from log_define import LogDefine

reload(sys)
sys.setdefaultencoding('utf8')


# logging.basicConfig(level=logging.INFO,
#   format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d",
#                stream=sys.stdout)

class ControlSftp():
    def __init__(self, host, port, username, password):  # 默认sftp地址
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        try:
            self.t = paramiko.Transport((self.host, self.port))
            self.t.connect(username=self.username, password=self.password)
            self.sftp = paramiko.SFTPClient.from_transport(self.t)
            # print('connect success!')
            LogDefine()  #
            logging.info("connect %s success!", self.host)
        except Exception, e:
            print e
            LogDefine()
            logging.error("connect %s has problem", self.host)

    def connect_sftp(self, host, port, username, password):
        try:
            t = paramiko.Transport((host, port))
            t.connect(username=username, password=password)
            paramiko.SFTPClient.from_transport(t)
            print('connect success!')
        except Exception, e:
            print e

    # 列出sftp指定路径下的内容
    def list_sftp(self, path):
        list = self.sftp.listdir(path)
        # print list
        for i in list:
            print i
        print('connect success!')

    # 上传本地路径上单个MP3(filename)到sftp指定目录下

    def sftp_put(self, filename, localpath, remotepath, path):
        # self.connect_sftp()
        self.sftp.chdir(path=path)
        try:
            # 搜索音乐目录找到所有的MP3文件路径所在目录赋值给localpath，根据MP3的路径名字给远程目录命名并上传
            self.sftp.put(localpath=localpath + filename, remotepath=remotepath + filename)  # 1774687688.mp3")
            song_ftppath = remotepath + filename
            # print "%s upload success" %filename
            LogDefine()
            logging.info("%s upload success", filename)
            return song_ftppath
        except Exception, e:
            print e
            logging.error("%s upload has problem", filename)
        finally:
            self.t.close()
            #print "Sftp Disconnect Success！"
            logging.info("Sftp Disconnect Success！")

