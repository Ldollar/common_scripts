#!/user/bin/env python
# -*- coding:utf-8 -*-
import json
import os

import time


def pinjie_dir(path_str=None):
    cwd_path=os.getcwd()
    #abs_path=os.path.abspath(cwd_path)
    dir_path=cwd_path+"\\"+path_str
    return dir_path

def mai_get_now_cwd():
    now_cwd=os.getcwd()
    return now_cwd


def mai_judge_dir(judge_path=None):
    #os.getcwd()
    return os.path.exists(judge_path)

def mai_mkdir_dir(mkdir_path=None):
    os.mkdir(mkdir_path)
    print u"make dir %s creating OK"%mkdir_path

def get_now_time():
    time1 = time.localtime()
    day_format=time.strftime("%Y%m%d",time1) #精确到天
    #time.strftime("%Y%m%d%H", time1) #精确到小时
    return day_format

#装饰器判断是否正确，选择相应的函数

def read_file(file_path=r"E:\programing\project\common_scripts\demo-txt.txt"):
    all_ids=[]
    with open(file_path,"r") as f:
        #print f.readlines()
        all_id = f.readlines()
        for i in all_id:
            all_ids.append(i.strip("\n "))
    return all_ids
def mai_mkfile(file_dir,filename):
    file_path=file_dir+"\\"+filename+".txt"
    return file_path

def mai_read_json(path="C:\Users\Administrator\Documents\Fiddler2\Captures\maidian123.json"):
    with open(path) as f:
        json_to_dict=json.load(f)
    return json_to_dict
def mai_analysis_json(jsonid,event_id,field="data"):


    if [jsonid][field]:
        pass
def mai_post_json_field_length(body_json,field="data"):
    length_field=(body_json[field])
    return length_field
