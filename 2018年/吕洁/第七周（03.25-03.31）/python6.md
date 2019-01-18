## 1.正则表达式                                
正则表达式是一种用来匹配字符串的工具，用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，就认为它“匹配”了。

\d：匹配一个数字

\w：匹配一个字母或数字

\s：匹配一个空格

.：匹配任意字符

*：表示任意个字符（包括0个）

+：表示至少一个字符

？：表示0个或1个字符

{n}：表示n个字符

{n,m}：表示n-m个字符

A|B：可以匹配A或B

^：表示行的开头

^\d：表示必须以数字开头

$：表示行的结束

\d$：表示必须以数字结束

要做更精确地匹配，可用[]表示范围，比如：

[0-9a-zA-Z\_]：可匹配一个数字、字母或者下划线

[0-9a-zA-Z\_]+：可匹配至少由一个数字、字母或者下划线组成的字符串

### re模块
re模块包含了一些有用的操作正则表达式的函数，其中一些重要的函数如下所示：

compile(pattern[,flags])：根据包含正则表达式的字符串创建模式对象

search(pattern,string[,flags])：在字符串中寻找模式

match(pattern,string[,flags])：在字符串的开始处匹配模式

split(pattern,string[,maxsplit=0])：根据模式的匹配项来分割字符串

findall(pattern,string)：列出字符串中模式的所有匹配项

sub(pat,repl,string[,count=0])：将字符串中所有pat的匹配项用repl替换

escape(string)：将字符串中所有特殊正则表达式字符转义

下面将介绍re匹配对象的一些重要方法。

group([gruop1,…])：获取给定子模式（组）的匹配项

start([gruop])：返回给定组的匹配项的开始位置

end([gruop])：返回给定组的匹配项的结束位置

span([group])：返回一个组的开始和结束位置

## 2.错误处理和单元测试
### 错误处理
在捕获错误时，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。一般采用try...except...finally...的错误处理机制，当认为某些代码可能会出错时，可用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

既能把错误栈打印出来，分析错误原因，同时能让程序继续执行，可用python内置的logging模块可以容易地记录错误信息。

    import logging
    def foo(s):
       return 10/int(s)
    def bar(s):
       return foo(s)*2
    def main():
       try:
          bar(‘0’)
       except Exception as e:
          logging exception(e)
    main()
    print(‘END’)	
出错后，程序打印完错误信息后会继续执行，并正常退出。

    $ python3 err_logging.py
    ERROR:root:division by zero
    Traceback (most recent call last):
       File "err_logging.py", line 13, in main bar('0')
       File "err_logging.py", line 9, in bar return foo(s) * 2
       File "err_logging.py", line 6, in foo  return 10 / int(s)
    ZeroDivisionError: division by zero
    END
在错误处理中，还可以用raise语句跑出一个错误的实例，raise语句如果不带参数，就会把当前错误原样抛出，此外，在except中raise一个Error，还可以把一个类型的错误转化成另一种类型。

    try:
        10 / 0
    except ZeroDivisionError:
        raise 
	raise后加Error
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')
### 单元测试
需要引入python自带的unittest模块，编写单元测试模块，其格式如下所示。

    import unittest
    class TestDict(unittest.TestCase):
	    def test_init(self):
            ...
        def test_key(self):
            ...
    if _name_==’_main_’:
        unittest.main()
编写单元测试时，需要编写一个测试类，从unittest.TestCase集成，以test开头的方法为测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

## 3.IO编程
读写文件是指请求操作系统打开一个文件对象，然后通过操作系统提供的接口从这个文件对象中读取数据，或者把数据写入这个文件对象。

### 读文件

    f=open(‘/path/to/file’,’r’)
    f.read()
    f.close()
如果要读取二进制文件，比如图片、视频等，用’rb’模式打开文件即可。用read(size)方法，每次最多可读取size个字节的内容，调用readline()可每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

### 写文件
写文件和读文件一样，唯一区别是调用open()函数时，传入标识符’w’或者’wb’表示写文本文件或写二进制文件。

    f=open(‘/path/to/file’,’w’)
    f.write()
    f.close()
在调用write()写入文件时，务必调用f.close()来关闭文件。在写文件的时候，操作系统往往不会立刻把数据写入磁盘中，而是放在内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。可用with语句来进行文件的写入,with语句可自动调用close()方法。

    with open('/Users/michael/test.txt', 'w') as f:
      f.write('Hello, world!')

### StringIO和BytesIO
在内存中读写时，可使用StringIO和BytesIO。

StringIO是在内存中读写str。

    from io import StringIO
    f = StringIO()
    f.write('hello')

    from io import StringIO
    f = StringIO('Hello!\nHi!\nGoodbye!')
    f.read()
BytesIO可在内存中读写二进制数据。

    from io import BytesIO
    f = BytesIO()
    f.write('中文'.encode('utf-8'))

    from io import BytesIO
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    f.read()
