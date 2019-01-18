import re
import operator as op


def compare(s1,s2): 
  #判断是否有空字符串
  if (len(s1)==0)|(len(s2)==0):
      return -2
  else:
    #判断是否是非法字符    
    if re.search(r"[^A-Za-z0-9]+", s1) or re.search(r"[^A-Za-z0-9]+", s2):
        return -2
    else:
        #分解字符串        
        find_lst1 = re.findall(r"(\d+)|([a-zA-Z]+)", s1)
        find_lst2 = re.findall(r"(\d+)|([a-zA-Z]+)", s2)
        
        #比较  
        for index in range(min(len(find_lst1),len(find_lst2))):
            #如果子串不一致
            if find_lst1[index]!=find_lst2[index]:
                #如果都是子字母串
                if (find_lst1[index][0]=='') & (find_lst2[index][0]==''):
                    if op.gt(find_lst1[index][1], find_lst2[index][1])==1:
                        return 1
                    else:
                        return -1
                #如果一个子字母串一个子数字串，子数字串小
                elif (find_lst1[index][0]=='') & (find_lst2[index][0]!=''):
                    return 1
                elif (find_lst1[index][0]!='') & (find_lst2[index][0]==''):
                    return -1
                #如果都是子数字串
                elif (find_lst1[index][0]!='') & (find_lst2[index][0]!=''):
                    if op.gt(int(find_lst1[index][0]), int(find_lst2[index][0])):
                        return 1
                    elif op.lt(int(find_lst1[index][0]), int(find_lst2[index][0])):
                        return -1
                    #如果相等，则要比较长短
                    elif op.eq(int(find_lst1[index][0]), int(find_lst2[index][0])):
                        if len(find_lst1[index][0])>len(find_lst2[index][0]):
                            return 1
                        else:
                            return -1
        #如果没有子串不一致，则比较子串的数量
        if len(find_lst1)>len(find_lst2):
            return 1
        elif len(find_lst1)<len(find_lst2):
            return -1
        elif len(find_lst1)==len(find_lst2):
            return 0

#判断输入的字符串大小
while(1):
  s1=input('输入第一个字符串：')
  s2=input('输入第二个字符串：')
  result=compare(s1,s2)
  print('字符串比较结果：',result)



