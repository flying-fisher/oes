# 1.import用法
从模块导入函数的时候，通常使用下面四种方法：

（1）import somemodule，使用somemodule.somefunction调用方法

（2）from somemodule import somefunction

（3）from somemodule import somefunction, anotherfunction.

（4）from somemodule import *

在语句末尾增加一个as子句，在该子句后给出想要使用的别名:

（1）为整个模块提供别名：import math as foobar

（2）为函数提供别名：from math import sqrt as foobar
# 2.赋值语句
（1）链式赋值：将同一个值赋给多个变量。x=y=3等同于y=3，x=y。

（2）增量赋值：将表达式运算符放置在赋值运算符的左边，对于*、/、%等运算符都适用。如x+=1；x*=2。

（3）序列解包：将多个值的序列解开，然后放到变量的序列中。

values=1,2,3

x,y,z=values

x

1
# 3.函数的定义和参数的性质  
在python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号，并在缩进块中编写函数体，函数的返回值用return语句返回。

（1）字符串作为参数

def  change(n):

        n=’Mr. Gumby’
name=’Mrs. Entity’

change(name)

name

’Mrs. Entity’

字符串、数字和元组作为参数时，其值是不可变的。具体运行过程如下：

name=’Mrs. Entity’

n=name  #传递参数

n=’Mr. Gumby’  #在函数内部完成

name

’Mrs. Entity’

（2）可变的数据结构作为参数

def  change(n):

        n[0]=’Mr. Gumby’
        
names=[’Mrs. Entity’, ’Mrs. Thing’]

change(names)

names

[’Mr. Gumby’, ’Mrs. Thing’]

当两个变量同时引用一个列表时，它们引用的是同一列表。具体运行过程如下：

names=[’Mrs. Entity’, ’Mrs. Thing’]

n=names  #传递参数

n[0]=’Mr. Gumby’

names

[’Mr. Gumby’, ’Mrs. Thing’]

如果想避免出现这种情况，可以复制一个列表的副本。
