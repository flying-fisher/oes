# -*- coding: utf-8 -*-
import re
import os
import operator
import sys


def myCompare(str_a, str_b):
    "主要是通过正则表达式完成对字母和数字的分离"
    #搜索是否有非法字符
    if re.search('\W', str_a) or re.search('\W', str_b):
        return -2
    while True:
        #通过正则表达式搜索子母串或数字串
        regex_a = re.search('[a-zA-z]+|[0-9]+',str_a)
        regex_b = re.search('[a-zA-z]+|[0-9]+',str_b)
        sub_a = regex_a.group() if regex_a else None
        sub_b = regex_b.group() if regex_b else None
        #子如果一边已无子串（子字母串或子数字串），另外一方还有子串，则无子串的小；如果双方均无子串，则相等
        if sub_a == None or sub_b == None:
            return compareLength(sub_a,sub_b)
        #如果被比较的都是子数字串，则按数值比较规则比较大小，如果值相等，则子数字串短的一方（前面的0少）小；
        elif re.match('[0-9]+', sub_a) and re.match('[0-9]+', sub_b):
            if compareNumbers(sub_a, sub_b):
                return compareNumbers(sub_a,sub_b)
        #如果被比较的都是子字母串，则按Python的cmp()的规则比较子字母串大小
        elif re.match('[a-zA-Z]+', sub_a) and re.match('[a-zA-z]+', sub_b):
            if compareLetters(sub_a, sub_b):
                return compareLetters(sub_a,sub_b)
        #如果被比较的一边是子数字串，一边是子字母串，则子数字串小
        elif re.match('[0-9]+', sub_a) and re.match('[a-zA-z]+', sub_b):
            return -1
        elif re.match('[a-zA-z]+', sub_a) and re.match('[0-9]+', sub_b):
            return 1
        #通过切片继续对两个字符串进行匹配
        str_a = str_a[len(sub_a):]
        str_b = str_b[len(sub_b):]
def compareLength(str_a, str_b):
    "长度的比较"
    if str_a == None and str_b == None:
        return 0
    elif str_a == None:
        return -1
    else:
        return 1
def compareNumbers(str_a,str_b):
    "按数值大小比较纯数字子串"
    if int(str_a) > int(str_b):
        return 1
    elif int(str_a) < int(str_b):
        return -1
    elif len(str_a) > len(str_b):
        return 1
    elif len(str_a) < len(str_b):
        return -1
    else:
        return 0
def compareLetters(str_a, str_b):
    '''按cmp()的规则比较纯字母子串'''
    if operator.eq(str_a, str_b):
        return 0
    elif operator.gt(str_a, str_b):
        return 1
    else: 
        return -1
if __name__ == '__main__':
    #对命令行参数形式的输入处理
    print("***************通过命令行参数形式输入两个字符串***************")
    if len(sys.argv) > 2:
        print("计算结果为:"+str(myCompare(sys.argv[1], sys.argv[2])))
    else:
        print("没有命令行形式的输入或输出有误")
    #从文件读取测试用例并输出到文件
    print("**************************************************************")
    print("************从input.txt读取输入并输出到output.txt*************")
    input_file = 'input.txt'
    output_file = 'output.txt'
    with open(input_file, 'r', encoding='UTF-8') as cin:
        with open(output_file, "w", encoding='UTF-8')as cout:
            for line in cin:
                line = line[:-1]#去掉输入文件中的换行符
                temp = line.split("\t")
                if len(temp) > 1:
                    cout.write(str(myCompare(temp[0], temp[1]))+'\n')
    print("读取并输出完成")
    print("**************************************************************")
    print("**********************手动输入并输出结果**********************")
    while input("是否进行输入(y/n)").lower() == 'y':
        a = input("请输入第一个字符串:")
        b = input("请输入第二个字符串:")
        print("字符串的比较结果为:"+str(myCompare(a, b)))
    print("**************************************************************")
