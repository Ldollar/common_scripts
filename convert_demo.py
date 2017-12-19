#!/user/bin/env python
# -*- coding:utf-8 -*-

# /usr/env/bin python
# -*- coding:utf-8 -*-
import functools

import os

jinzhi={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,
        "C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,
        "L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,
        "W":32,"X":33,"Y":34,"Z":35,"a":36,"b":37,"c":38,"d":39,"e":40,"f":41,"g":42,
        "h":43,"i":44,"j":45,"k":46,"l":47,"m":48,"n":49,"o":50,"p":51,"q":52,"r":53,
        "s":54,"t":55,"u":56,"v":57,"w":58,"x":59,"y":60,"z":61,"@":62,"#":63}
jinzhi_reverse={}

#print jinzhi.keys()
for i in jinzhi.keys():
    #print i
    jinzhi_reverse[str(jinzhi[i])] = i
#print jinzhi_reverse

Base64={"A":0,"B":1, "C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,
        "L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,
        "W":22,"X":23,"Y":24,"Z":25,"a":26,"b":27,"c":28,"d":29,"e":30,"f":31,"g":32,
        "h":33,"i":34,"j":35,"k":36,"l":37,"m":38,"n":39,"o":40,"p":41,"q":42,"r":43,
        "s":44,"t":45,"u":46,"v":47,"w":48,"x":49,"y":50,"z":51,"0":52,"1":53,"2":54,
        "3":55,"4":56,"5":57,"6":58,"7":59,"8":60,"9":61,"+":62,"/":63}

Base64_reverse={}
for i in Base64.keys():
    #print i
    Base64_reverse[str(Base64[i])] = i
def judge_range(func):
    """判断进制的取值范围,比如7进制的取值范围为0-6，大于9从A开始取值"""
    @functools.wraps(func)
    def check_out(self,input_mode,input_value,output_mode):
        flag = True
        for i in xrange(0,len(str(input_value))):
            #print input_value[i]
            #if int(input_value[i]) < input_mode:
            if int(input_mode) != 64 and int(output_mode)!=64:
                if int(jinzhi[input_value[i]])< int(input_mode):
                    print jinzhi[input_value[i]]
                    pass

                else:
                    #print 111222222
                    #print u"%s进制的取值范围小于 %s"%(input_mode,input_mode)
                    flag = False
            else:
                if Base64[input_value[i]] < int(input_mode):
                    # print jinzhi[input_value[i]]
                    pass

                else:
                    # print 111222222
                    # print u"%s进制的取值范围小于 %s"%(input_mode,input_mode)
                    flag = False
        if flag:
            return func(self,input_mode,input_value,output_mode)
        else:
            print u"%s进制的取值范围小于 %s" % (input_mode, input_mode)

    return check_out


def input_value_to_list(func):
    @functools.wraps(func)
    def check(self,input_mode, input_value, output_mode):
        list = []
        if int(input_mode) != 64 and int(output_mode)!=64:
            for i in xrange(0, len(input_value)):
                #print jinzhi[input_value[i]]
                list.append(str(jinzhi[input_value[i]]))  # 把大于9的转换成数字
                # if int(input_value[i]) < input_mode:
            input_value = list
            #print input_value
            return func(self,input_mode, input_value, output_mode)
        else:
            for i in xrange(0, len(input_value)):
                #print jinzhi[input_value[i]]
                list.append(str(Base64[input_value[i]]))  # 把大于9的转换成数字
                # if int(input_value[i]) < input_mode:
            input_value = list
            #print input_value
            return func(self,input_mode, input_value, output_mode)
    return check





class ConvertDemo():
    def __init__(self):
        pass


    @judge_range
    def binary_to_decimal(self,input_mode=2,input_value="1000",output_mode=10):
        len_value=len(input_value)
        output_value = 0
        for i in xrange(0,len_value):
            #print -i-1
            output_value += int(input_value[-i-1])*2**i
        print output_value


    @judge_range
    def decimal_to_binary(self,input_mode=10,input_value="2",output_mode=2):
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
            yushu_list.append(jinzhi_reverse[str(yu)])
        #print yushu_list
        for i in xrange(0,len(yushu_list)):

            output_value = output_value+str(yushu_list[i])
        #print output_value[::-1]
        output_value = output_value[::-1]
        print output_value
        return output_value

    @judge_range
    @input_value_to_list
    def shiliu_to_binary(self,input_mode=10,input_value="1A",output_mode=2):
        out_value_1=[]
        output_value_2=""
        for i in input_value:
            value = int(i)
            yushu_list = []
            # print value / 2
            # print value % 2
            flag = value
            output_value = ""
            while flag != 0:
                yu = flag % 2
                flag = flag / 2
                # print flag,yu
                yushu_list.append(str(yu))
            # print yushu_list
            for i in xrange(0, len(yushu_list)):
                output_value = output_value + str(yushu_list[i])
            # print output_value[::-1]
            output_value = output_value[::-1]
            out_value_1.append(output_value)
        for j in out_value_1:
            #print j
            tmp = None
            list1 = []
            if len(j)<4:
                reverse_list = j[::-1]
                #print type(list(reverse_list))
                list1 = list(reverse_list)
                #print reverse_list
                for z in xrange(0,4):
                    #print z
                    try:
                        #pass
                        list1[z]
                    except:
                        list1.append(0)
                tmp = list1[::-1]
                #print tmp
                for i in tmp :
                    #print i
                    output_value_2 += str(i)
                #print output_value_2
            else:
                output_value_2 += str(j)
        print output_value_2


        #print out_value_1
        return output_value



    def liushisan_to_decimal(self,input_mode=63,input_value="z",output_mode=10):
        len_intput_value = len(input_value)
        output_value = 0
        for i in xrange(0,len_intput_value):
            output_value += int(jinzhi[input_value[-i-1]])*63**i  #参考16进制10进制
            #print output_value
        return output_value
    @judge_range
    @input_value_to_list
    def liushisi_to_decimal(self,input_mode=63,input_value="+",output_mode=10):   #需引用64进制编码表Base64
        output_value = 0
        for i in xrange(0,len(input_value)):
            #print i
            output_value += int(input_value[-i - 1]) * 64 ** i  # 参考16进制10进制
        #print output_value
        return output_value

        # return output_value
    @judge_range
    @input_value_to_list
    def inputmode_to_decimal(self,input_mode=63,input_value="+",output_mode=10):   #不包含64进制
        output_value = 0
        for i in xrange(0, len(input_value)):
            #print i
            output_value += int(input_value[-i - 1]) * int(input_mode) ** i  # 参考16进制10进制
        #print output_value
        return output_value

    #高进制转低进制？

    def decimal_to_low(self,input_mode=10,input_value="98",output_mode=8):   #参考十进制转二进制,主要是转成几进制就用几去除
        if input_value:
            value = int(input_value)
            yushu_list = []
            # print value / 2
            # print value % 2
            flag = value
            output_value = ""
            if int(output_mode) !=64:
                while flag != 0:
                    yu = flag % int(output_mode)
                    flag = flag / int(output_mode)
                    #print flag,yu
                    yushu_list.append(jinzhi_reverse[str(yu)])
                #print yushu_list
            else:
                while flag != 0:
                    yu = flag % int(output_mode)
                    flag = flag / int(output_mode)
                    #print flag,yu
                    yushu_list.append(Base64_reverse[str(yu)])
            for i in xrange(0, len(yushu_list)):
                output_value = output_value + str(yushu_list[i])
            # print output_value[::-1]
            output_value = output_value[::-1]
            #print output_value
            return output_value


    def low_to_high(self,input_mode_low=8,input_value="78",output_mode_high=16):
        value1=self.decimal_to_binary(input_mode=input_mode_low,output_mode=2)
        print value1


    """通常A进制转换B进制：先将A进制转换为十进制，再将十进制转化为B进制"""

    #aaa=inputmode_to_decimal(input_mode=52,input_value="15",output_mode=10)
    #decimal_to_low(input_mode=10,input_value=aaa,output_mode=54)
def main(inputMode,inputValue,outputMode):
    demo = ConvertDemo()
    if int(inputMode) != 64:
        #print 111111111111111
        temporary = demo.inputmode_to_decimal(input_mode=inputMode,input_value=inputValue,output_mode=10)
        result1=demo.decimal_to_low(input_mode=10,input_value=temporary,output_mode=outputMode)
        print result1
    elif int(inputMode) == 64 and int(outputMode) == 10:
        result2=demo.liushisi_to_decimal(input_mode=inputMode, input_value=inputValue, output_mode=10)
        print result2
    elif int(inputMode) == 64 or int(outputMode) == 64:
        temp = demo.liushisi_to_decimal(input_mode=inputMode, input_value=inputValue, output_mode=10)
        result3=demo.decimal_to_low(input_mode=10, input_value=temp, output_mode=outputMode)
        print result3



if __name__=="__main__":
    print (u"此脚本实现任意进制之间的转化，请输入你要input_mode--input_value--out_mode,")

    input = raw_input(unicode('请输入你要转换的进制，如十进制请输入10 :', 'utf-8').encode('gbk'))
    #print input
    output = raw_input(unicode('请输入你要转换成的进制，如二进制请输入2 : ', 'utf-8').encode('gbk'))
    value= raw_input(unicode('请输入你要转换的值 如 "1280" (此值是一个字符串) : ', 'utf-8').encode('gbk'))
    #print value
    main(inputMode=input,inputValue=value,outputMode=output)
    os.system("pause")
#binary_to_decimal()
#decimal_to_binary(input_mode=10,input_value="4593")
#liushisan_to_decimal()
# liushisi_to_decimal()
#inputmode_to_decimal(input_mode=16,input_value="1F2A",output_mode=10)
#hign_to_low(input_mode=10,input_value="485",output_mode=8)
#arbitrary_to_binary(input_mode=16,input_value="1000",output_mode=2)

#shiliu_to_binary(input_mode=16,input_value="2AF5",output_mode=2)