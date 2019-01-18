# 环境配置

1.  需要各种python库，但不需要一个一个安装。用一个集成环境anaconda

2.  anaconda下载链接：*www.continuum.io/downloads/*

3.  Anaconda既帮助安装了python，也安装了很多库

4.  课程推荐直接装python3.6，不过anaconda下载比较慢，下载到exe文件，一直下一步就安装完成了。

5.  Anaconda的可执行程序：

    a.  Anaconda prompt：和cmd差不多，只需要用几个命令：

        i.  conda list：列出anaconda已经安装好的库和版本

        ii. conda install xxx：安装xxx这个库

        iii. conda update xxx：更新xxx这个库

    b.  Jupyter Notebook：写代码的地方，编译的环境：

        i.  相当于写python的浏览器版本

        ii. 新建文件夹或文件可以在右上角new一个

# Python快速入门

1.  对一门新语言的学习，先把重要的地方搞定，并不需要扣得非常细，等到真正做项目的时候再深入细节。这样比较科学

# 变量类型

1.  days = 365，等号左边标识符，右边值，可以做到直接创建变量并赋值

2.  无需指定类型，自动根据后面赋的值指定类型

3.  Python不需要用；作为代码的结尾了

4.  在标识符中，下划线\_可以用于划分标识符，如days\_1，days\_2；或者把一个类似于句子的标识符连接起来number\_of\_days

5.  打印函数print(days)，或print(‘hello world’)，或print(365)。就在屏幕上显示

    a.  Python2版本不需要括号

    b.  Python3版本必须括号

    c.  String值可以通过双引号或单引号

6.  Python区分变量的数据类型

    a.  type(标识符)：可以打印标识符的数据类型所属的类

# LIST基础

1.  类型转换：

    a.  字符串转整型：int(“8”)

    b.  整型转字符串：str(8)

    c.  要能转换的才能转，否则会报错

        i.  比如int(“exam”)就不能

2.  运算符+-\*/和其他的一样

    a.  指数级运算可以用2\*\*3=8

    b.  而其他语言则是pow(2,3)

3.  List对应于其他语言的数组，但是更方便

    a.  months = \[\] 即完成了list的声明

    b.  可以动态地在list添加元素：months.append(“January”)

    c.  List中可以有混合数据类型，可以同时添加整型和字符串等

# List索引

1.  list的索引和其他语言一样，是从0开始的

2.  返回list中元素个数：len(list)

    a.  类似于java的a.length

3.  list\[len(list) - 1\]可以打印最后一个元素

    a.  同样可以通过从后往前数：list\[-1\]打印最后一个元素

        i.  同样的，list\[-2\]就是倒数第二个元素

4.  对list取切片的方法：

    a.  list\[2:5\]：取出了list中的第3、4、5号元素，同样是一个list

    b.  切片是取头不取尾，左闭右开

    c.  也可以list\[2:\]：取出list中第3号元素以及之后的所有元素

# 循环结构

1.  for循环：

    for city in cities：

    print(city)

2.  其中cities是要进行遍历的集合结构，city是给当前遍历的元素起的变量名

3.  While循环：

    i = 0

    while i &lt; 3:

    i += 1

    print (i)

4.  Python一个重要的地方是通过缩进进行结构的控制，和其他语言通过大括号不同

    a.  缩进可以是4个空格，或者一个tab，但从头到尾只能用其中一种

5.  for循环的range表示：

    for i int range(10):

    print (i)

    a.  进行10次迭代

6.  List可以多层嵌套，而for循环也可以多层嵌套，和JAVA类似

    a.  List中嵌套的list的数据类型、长度等没有限制，可以各不相同

# 判断结构

1.  bool类型值的定义

    a.  A = True

    b.  B = False

2.  和java不同，通过==和!=判断对象相同只看值，不看地址

    a.  print(“abc” == “abc)输出True

3.  if/else语句：

    if True/False:

    xxx

    else:

    xxx

    a.  其中True和False可以是预先声明的bool型变量

# 字典

1.  找一个元素是否存在一个集合里有三种方法：

    a.  第一种：

        for animal in animals:

        if animal == ‘cat’:

        print(“cat found”)

    b.  第二种：

        if ‘cat’ in animals:

        print(“cat found”)

    c.  第三种：

        a = ‘cat’ n animals

        print(a)

<!-- -->

2.  字典的定义是scores = {}，和list的\[\]稍有不同

    a.  值通过scores\[“jim”\] = 80这样的方式添加键值对

    b.  print(scores.keys())打印所有键作为list

    c.  print(scores)打印所有键值对，键和值通过冒号分割

    d.  字典的优势是可以通过键直接找到值

        i.  print(scores\[“jim”\])可以打印出80

    e.  可以初始化直接加入键值对：

        Students = {

        “Tom” : 60,

        “Jim” : 70

        }

        i.  不同键值对直接用逗号分割

    f.  可以直接对某个键的值进行更改：

        Students\[“Tom”\] = 65

# 文件操作

1.  打开文件：

    f = open(“test.txt”,”r”)

    a.  如果打开的文件和程序在一个路径下，则可以不指定路径，否则必须用绝对路径

    b.  r表示以只读的方式打开文件

        i.  如果该模式下文件不存在会报错

    c.  w表示以写的方式打开文件

        i.  如果该模式下文件不存在会自动创建

2.  读取文件所有内容：

    a.  g = f.read()，返回一个字符串

3.  关闭文件：

    a.  f.close()

    b.  用完文件记得关闭，否则其他用户程序打开时会起冲突

4.  写文件：

    a.  f.write(“123”)

    b.  write默认以追加的方式，而不是覆盖

5.  str.split(“,”)：根据参数对字符串进行切分

# 函数基础

1.  定义函数:

    def printHello():

    print(“hello”)

2.  带冒号后基本就需要靠缩进进行结构的划分了

3.  可以不要参数，也可以有多个参数，和Java一样


