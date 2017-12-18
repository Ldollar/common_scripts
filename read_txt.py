#!/user/bin/env python
#coding=utf8
import csv
import re

def find_percentage(text=None,rex_str=None):
    rule ="User (\d+)%, System (\d+)%"
    pattern = re.compile(rule,re.I)
    result = re.findall(pattern,text)
    if result:
        find = result[0]
        print find
        return find
def find_message(res=None):
    rule = 'Total RAM: (\d+) kB'
    #rule = "User (\d+)%, System (\d+)%"  # CSV文件是否添加双引号问题
    pattern = re.compile(rule,re.I)
    result = re.findall(pattern, res)

    if len(result)>0:
        #print result[0]
        return result
        #print "find_message:",result
    else:
        pass
        #return None
# with open("E:\LOG\cpu.txt") as f:
#     #print f.read()
#     writer = csv.writer(file('E:\LOG\your.csv', 'wb'))
#     writer.writerow(['user', 'system'])
#     for line in f.readlines():
#         s = find_message(res=line)
#         #print s
#         if s !=None :
#             writer.writerow(s)

with open("E:\LOG\meminfo.txt") as f:
    #print f.read()
    writer = csv.writer(file('E:\LOG\\Total.csv', 'wb'))
    writer.writerow(['Total'])
    for line in f.readlines():
        s = find_message(res=line)
        #print s
        if s !=None :
            writer.writerow(s)
