# -*- coding: utf-8 -*-

import re


class Solution:

    # �Ƚ��ַ�����С
    def cmpstr(self, str1, str2):
        if self.isvalid(str1, str2):    # �Ϸ������ʼ�Ƚ�
            return self.cmpfromleft(str1, str2)
        else:                           # ���Ϸ�����-2
            return -2

    # �ж����ַ����Ƿ�Ϸ�
    def isvalid(self, str1, str2):
        if str1.isalnum() and str2.isalnum():
            return True
        else:
            return False

    # ����һ�Ӵ���ʼ�Ƚ�
    def cmpfromleft(self, str1, str2):
        # base case
        if str1=='' and str2=='':
            return 0
        elif str1 == '':
            return -1
        elif str2 == '':
            return 1
        # ȡ��һ�Ӵ�
        p = re.compile('[\d]+|[a-zA-Z]+')
        lsubstr1 = p.findall(str1)[0]
        lsubstr2 = p.findall(str2)[0]
        # �Ƚ���һ�Ӵ�
        res = self.cmpsubstr(lsubstr1, lsubstr2)
        if res != 0:       # �����һ�Ӵ�����, ���رȽϽ��
            return res
        else:            # �����һ�Ӵ���ȣ������Ƚ�ʣ�ಿ��
            return self.cmpfromleft(str1.lstrip(lsubstr1), str2.lstrip(lsubstr2))

    # �Ƚ��Ӵ�
    def cmpsubstr(self, str1, str2):
        if str1.isdigit() and str2.isalpha():
            return -1
        elif str1.isalpha() and str2.isdigit():
            return 1
        elif str1.isdigit() and str2.isdigit():
            return self.cmpnumber(str1, str2)
        else:
            return self.cmpletter(str1, str2)

    # �Ƚ������Ӵ�
    def cmpnumber(self, str1, str2):
        if int(str1) > int(str2):
            return 1
        elif int(str1) < int(str2):
            return -1
        else:
            return cmp(len(str1),len(str2))

    # �Ƚ���ĸ�Ӵ�
    def cmpletter(self, str1, str2):
        return cmp(str1, str2)

if __name__ == '__main__':

    solution = Solution()

    while True:
		print '****************** ���ַ����ȽϿ�ʼ ******************'
		str1 = raw_input('�������һ���ַ���: ')
		str2 = raw_input('������ڶ����ַ���: ')
		print solution.cmpstr(str1, str2)