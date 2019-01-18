# -*- coding: utf-8 -*-

import re


class Solution:

    # 比较字符串大小
    def cmpstr(self, str1, str2):
        if self.isvalid(str1, str2):    # 合法则从左开始比较
            return self.cmpfromleft(str1, str2)
        else:                           # 不合法返回-2
            return -2

    # 判断两字符串是否合法
    def isvalid(self, str1, str2):
        if str1.isalnum() and str2.isalnum():
            return True
        else:
            return False

    # 从左一子串开始比较
    def cmpfromleft(self, str1, str2):
        # base case
        if str1=='' and str2=='':
            return 0
        elif str1 == '':
            return -1
        elif str2 == '':
            return 1
        # 取左一子串
        p = re.compile('[\d]+|[a-zA-Z]+')
        lsubstr1 = p.findall(str1)[0]
        lsubstr2 = p.findall(str2)[0]
        # 比较左一子串
        res = self.cmpsubstr(lsubstr1, lsubstr2)
        if res != 0:       # 如果左一子串不等, 返回比较结果
            return res
        else:            # 如果左一子串相等，继续比较剩余部分
            return self.cmpfromleft(str1.lstrip(lsubstr1), str2.lstrip(lsubstr2))

    # 比较子串
    def cmpsubstr(self, str1, str2):
        if str1.isdigit() and str2.isalpha():
            return -1
        elif str1.isalpha() and str2.isdigit():
            return 1
        elif str1.isdigit() and str2.isdigit():
            return self.cmpnumber(str1, str2)
        else:
            return self.cmpletter(str1, str2)

    # 比较数字子串
    def cmpnumber(self, str1, str2):
        if int(str1) > int(str2):
            return 1
        elif int(str1) < int(str2):
            return -1
        else:
            return cmp(len(str1),len(str2))

    # 比较字母子串
    def cmpletter(self, str1, str2):
        return cmp(str1, str2)

if __name__ == '__main__':

    solution = Solution()

    while True:
		print '****************** 两字符串比较开始 ******************'
		str1 = raw_input('请输入第一个字符串: ')
		str2 = raw_input('请输入第二个字符串: ')
		print solution.cmpstr(str1, str2)