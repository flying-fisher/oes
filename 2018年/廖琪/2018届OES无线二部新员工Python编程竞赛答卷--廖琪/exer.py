import re

def CmpLAN(str1,str2):
    '''
    function: to compare two string2 which can be totally letters or numbers
    input: two strings which can be totally letters or numbers
    output: follow rules, if str1 > str2,return 1; if str1 < str2,return -1; else return 0
    '''
    if str1.isdigit() and str2.isdigit():
        num1 = int(str1)
        num2 = int(str2)
        if num1>num2:
            return 1
        elif num1<num2:
            return -1
        else:
            if len(str1) > len(str2):
                return 1
            elif len(str1) < len(str2):
                return -1
            else:
                return 0
    elif str1.isalpha() and str2.isalpha():
        return cmp(str1,str2)
    else:
        if str1.isdigit():
            return -1
        else:
            return 1

def CmpList(L1,L2):
    '''
    function: to compare two lists which include strings that are totally letters or numbers
    input: two lists which include strings that are totally letters or numbers
    output: follow rules, if L1 > L2,return 1; if L1 < L2,return -1; else return 0
    '''
    len1=len(L1)
    len2=len(L2)
    index1=0
    index2=0
    while not (index1==len1 or index2==len2): 
        tmp1 = L1[index1]
        tmp2 = L2[index2]
        result = CmpLAN(tmp1,tmp2)
        if result == 0:
            index1+=1
            index2+=1
        elif result ==1:
            index2+=1
        else:
            index1+=1
    if index1==len1 and index2==len2:
        return 0
    elif index1==len1:
        return -1
    else:
        return 1
               
def CmpStr(str1,str2):
    '''
    function: to compare two strings which only include letters and numbers
    input: two strings which only include letters and numbers
    output: follow rules, if str1 > str2,return 1; if str1 < str2,return -1; else return 0
    '''
    if not (str1.isalnum() and str2.isalnum()):
        return -2
    rule = re.compile(r'\d+|[a-zA-Z]+')
    str1_list = rule.findall(str1)
    str2_list = rule.findall(str2)
    return CmpList(str1_list,str2_list)

def main():    
    while True:    
        print '================ Compare begin ================\n'
        str1 = raw_input('Please input a string with letters and numbers: ')
        str2 = raw_input('\nPlease input a string with letters and numbers: ')
        result = CmpStr(str1,str2)    
        print '\nThe result is: %s \n' % result    
        print '================ Compare finished =============\n'
        
if __name__=='__main__':
    main()