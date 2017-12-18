# /usr/env/bin python
# -*- coding:utf-8 -*-

def convert(input_mode,input_value,output_mod):
    if input_mode == 2:
        pass



def binary_to_decimal(input_mode=2,input_value="1000",output_mode=10):
    len_value=len(input_value)
    output_value = 0
    for i in xrange(0,len_value):
        output_value += int(input_value[-i-1])*2**i
    print output_value
def decimal_to_binary(input_mode=10,input_value="150",output_mode=2):
    value = int (input_value)
    yushu_list=[]
    #print value / 2
    #print value % 2
    flag = value
    output_value = ""
    while flag != 0 :
        yu = flag % 2
        flag = flag / 2
        #print flag,yu
        yushu_list.append(yu)
    #print yushu_list
    for i in xrange(0,len(yushu_list)):

        output_value = output_value+str(yushu_list[i])
    #print output_value[::-1]
    output_value = output_value[::-1]
    return output_value
def liushisan_to_decimal(input_mode=63,input_value="150",output_mode=10):
    pass





#binary_to_decimal()
decimal_to_binary()
