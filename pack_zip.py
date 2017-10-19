#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from zipfile import *
import zipfile


# 解压zip文件
def unzip(source_zip,target_dir):
    myzip = ZipFile(source_zip)
    myfilelist = myzip.namelist()
    for name in myfilelist:
        f_handle = open(target_dir + name, "wb")
        f_handle.write(myzip.read(name))
        f_handle.close()
    myzip.close()


# 添加文件到已有的zip包中
def addzip(filename,file_zip):
    f = zipfile.ZipFile(file_zip, 'w', zipfile.ZIP_DEFLATED)
    f.write(filename)
    f.close()


# 把整个文件夹内的patch文件打包
def adddirfile(pack_zip_path,zipname):
    os.chdir(pack_zip_path)
    f = zipfile.ZipFile(zipname, 'w')
    for dirpath, dirnames, filenames in os.walk(pack_zip_path):
        for filename in filenames:
            if filename.split(".")[1] =="patch":
                f.write(filename)
    f.close()
    return zipname

