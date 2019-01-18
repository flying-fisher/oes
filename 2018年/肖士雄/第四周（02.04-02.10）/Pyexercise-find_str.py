'''
This is Python exercise. 
The description:
Give a origin string and a target string, find the start position. 
The target may be duplicate in the origin string.

@author: xiaoguan
'''
import os

a = input('Input:').split()
haystack = a[0]
needle = a[1]
def same(a,list1,list2):
    count = len(list2)
    for i in range(0,count):
        if list1[i + a] != list2[i]:
            return False
    return True
def find(haystack,needle):
    if needle == '':
        return [0]
    if haystack == '' and needle != '':
        return [-1]
    re = []            
    count1 = len(haystack)
    count2 = len(needle)
    for i in range(0,count1 - count2 + 1):
        if haystack[i] == needle[0]:
            if same(i,haystack,needle):
                re.append(i)
    if re == []:
        return [-1]
    else:
        return re
re = find(haystack,needle)
for i in re:
    print(i)
os.system('pause')