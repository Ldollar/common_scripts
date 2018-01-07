#-*- coding: UTF-8 -*-
#!/usr/bin/env python
import json
import sys

import re


def get_first_argv(path=None):
    sys.argv[1]
    with open(sys.argv[1]) as f:
        return f.readlines()

def find_char(list,func):
    for i in list:
        pass#print len(i.strip("\n "))



def match_string(rules=None, text=None):

    try:
        print rules
        pattern = re.compile(rules, re.I)
        result = re.findall(pattern, text)
        count = len(result)
        print result, count
        get_type_MM = result.group(1)
        return get_type_MM.split(",")
    except Exception, e:
        print "%s had not found "% rules
        return None
    count = None

def main():
    list = get_first_argv()
    for i in list:
        #print i
        Str = i.strip("\n ")
        match_string(rules=Str,text=sys.argv[2])

main()
