# 一、 正则表达式定义 #
正则表达式，又称正规表示式、正规表示法、正规表达式、规则表达式、常规表示法（英语：Regular Expression，在代码中常简写为regex、regexp或RE），计算机科学的一个概念。正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些匹配某个模式的文本。
正则表达式通常缩写成“regex”，单数有regexp、regex，复数有regexps、regexes、regexen。
# 二、举例介绍 #
## 例1 ##
    import re
    
    key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
    p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
    pattern1 = re.compile(p1)#我们在编译这段正则表达式
    matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
    print matcher1.group(0)#打印出来
上述代码返回值为“hello world”

## 例2 ##
假设我们的想法是把一个字符串中的所有"python"给匹配到。我们试一试怎么做
    import re
    
    key = r"javapythonhtmlvhdl"#这是源文本
    p1 = r"python"#这是我们写的正则表达式
    pattern1 = re.compile(p1)#同样是编译
    matcher1 = re.search(pattern1,key)#同样是查询
    print matcher1.group(0)
注意：正则表达式匹配是区分大小写的，如果上述的“python”写为“Python”的话，就无法匹配的到
## re 模块 ##
    re模块使 Python 语言拥有全部的正则表达式功能。其主要的方法有：
    match(正则表达式，待匹配字符串)
    search(正则表达式，待匹配字符串)
    compile(规则)
    group(num=0)
    findall（待匹配字符串）findall返回的是所有符合要求的元素列表，包括仅有一个元素时，它还是给你返回的列表。



## re.match与re.search的区别 ##
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

    实例
    #!/usr/bin/python
    import re
    line = "Cats are smarter than dogs";
    matchObj = re.match( r'dogs', line, re.M|re.I)
    if matchObj:
      print "match --> matchObj.group() : ", matchObj.group()
    else:
       print "No match!!"
    matchObj = re.search( r'dogs', line, re.M|re.I)
    if matchObj:
       print "search --> matchObj.group() : ", matchObj.group()
    else:
       print "No match!!"
    以上实例运行结果如下：
    No match!!
    search --> matchObj.group() :  dogs

## 正则表达式##
    正则表达式	代表的匹配字符
    [0-9]	0123456789任意之一
    [a-z]	小写字母任意之一
    [A-Z]	大写字母任意之一
    \d	等同于[0-9]
    \D	等同于[^0-9]匹配非数字
    \w	等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
    \W	等同于[^a-z0-9A-Z_]等同于上一条取非

    元字符	说明
    .	代表任意字符
    |	逻辑或操作符
    [ ]	匹配内部的任一字符或子表达式
    [^]	对字符集和取非
    -	定义一个区间
    \	对下一字符取非（通常是普通变特殊，特殊变普通）
    *	匹配前面的字符或者子表达式0次或多次
    +	匹配前一个字符或子表达式一次或多次
    ?	匹配前一个字符或子表达式0次或1次重复
    {n}	匹配前一个字符或子表达式
    {m,n}	匹配前一个字符或子表达式至少m次至多n次
    {n,}	匹配前一个字符或者子表达式至少n次
    {n,}?	前一个的惰性匹配
    ^	匹配字符串的开头
    \A	匹配字符串开头
    $	匹配字符串结束
    [\b]	退格字符
    \c	匹配一个控制字符
    \d	匹配任意数字
    \D	匹配数字以外的字符
    \t	匹配制表符
    \w	匹配任意数字字母下划线
    \W	不匹配数字字母下划线