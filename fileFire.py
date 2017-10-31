#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#当文件存在时报错
from moviepy import video

from make_checksum import md5_file

def file_rename(filepath,res,newfilename):
    """

     :param filepath: 文件所在路径
     :param res: 指定匹配的  '.'+文件后缀
     :param newfilename:
     :return:
     """

    os.chdir(filepath)
    for filename in os.listdir(filepath):
        if os.path.splitext(filename)[1] == res:    # res  格式".zip"
            oldfilename = filename
    oldname = filepath+oldfilename
    newname = filepath+newfilename
    os.rename(oldname,newname)
    return newname


def get_need_list(path,rex):
    """

    :param path: 文件所在路径
    :param rex: 匹配指定的后缀名   eg '.patch'
    :return: 返回list为符合的文件
    """
    file_patch_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == rex:      # rex  格式为".patch":
                allpath=os.path.join(dirpath, filename)
                file_patch_list.append(allpath)
    return file_patch_list


def get_file_checksum(files):

    for ii in files:
        cheksm=md5_file(ii)
        print cheksm

