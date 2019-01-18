# 快速入门

## 1. 输出语句print

- 在交互式解释器中，可以用print语句输出，也可以使用变量名查看变量的值。

	``` python
	>>> print 'hello world!'
	hello world!
	```

	``` python
	>>> str = 'hello world!'
	>>> str
	'hello world!'
	```

- print语句与字符串格式操作符（%）结合
	
	``` python
	>>> print "%s is String, %d is int, %f is float" % ("abc", 1, 1.0)
	abc is String, 1 is int, 1.000000 is float
	```

- 重定向输出到文件，符号 >>
	
	``` python
	>>> print >> filename, 'string'
	```

## 2. 输入语句 raw_input()

- 内建函数raw_input()读取标准输入，数据赋值给指定变量。

	``` python
	>>> user = raw_input('Enter your name: ')
	Enter your name: chensiwen
	>>> print 'Your name is: ', user
	Your name is:  chensiwen
	```

- 内建函数int()将字符串转成整型值。

	``` python
	>>> num = raw_input('Enter a number: ')
	Enter a number: 1000
	>>> print 'Your number is %d' % (int(num))
	Your number is 1000
	>>> print 'Your number is ', int(num)
	Your number is  1000
	>>> print 'Double your number is ', int(num)*2
	Double your number is  2000
	```

## 3. 帮组函数 help(函数名称)

```
	>>> help(raw_input) #以raw_input()函数为例
	Help on built-in function raw_input in module __builtin__:
	
	raw_input(...)
	    raw_input([prompt]) -> string
	    
	    Read a string from standard input.  The trailing newline is stripped.
	    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
	    On Unix, GNU readline is used if enabled.  The prompt string, if given,
	    is printed without a trailing newline before reading.
```

## 4. 注释

- 单行注释：注释语句从#字符开始，可以在一行的任何地方。
	
	``` python
	>>> # one comment
	```

- 文档字符串注释，在模块、类或者函数的起始添加一个字符串，起到在线文档的功能。文档字符串可以在运行时访问，也可以用来自动生成文档。

	```python
	>>> def foo():
		"this is a doc string"
		return true
	```

	Python提供一个机制，通过__doc__特别变量，动态获得文档字串。在模块、类、函数声明中第一个没有赋值的字符串可以用属性 `obj.__doc__` 来进行访问，其中 obj 是一个模块、类、函数名字，这在运行时也可以进行。	

## 5. 操作符

1. 标准算术操作符： 加(`+`)，减(`-`)，乘(`*`), 除（`/`, `//`)，取余(`%`)，指数(`**`)

	- 优先级：指数(`**`), 单目 `+`(正数)或 `-`(负数), 乘除法和取余，加减法
	
	```python
	>>> print -2*4+2**3
	0 
	```

	- 单斜杠 `/` ：python3.0以后，真除法，无论任何类型都会保持小数部分。
	- 双斜杠 `//` ：结果只取整数部分，若操作时是浮点型，结果是浮点型整数
	
	```python
	>>> 17 / 3  # int / int -> int
	5
	>>> 17 / 3.0  # int / float -> float
	5.666666666666667
	>>> 17//3
	5
	>>> 17 // 3.0  # explicit floor division discards the fractional part
	5.0
	```

2. 标准比较操作符： `<`, `>`, `<=`, `>=`, `==`, `!=`, `<>`

	- 返回布尔类型值：**`True`**, **`False`**
	- 两种不等于：`!=`, `<>` 后者在python3.0已不可用。

3. 逻辑操作符：`and`, `or`, `not`

	- 逻辑操作符可以将任意表达式连接在一起，并得到布尔值。
	- `A < B < C` 等价与 `A < B and B < C` 

## 6. 赋值

1. Python是动态类型语言，不需要预先声明变量的类型。变量的类型和值在赋值时被初始化
2. 赋值操作符(**`=`**)：在python中，对象是通过**引用**传递。是将对象的引用（并不是值）赋值给变量。可以链式赋值：
	
	```python
	y = x = x + 1
	```

3. 增量赋值：算术操作符与等号组合，结果赋值给左边变量。
	
	+=，-=，*=，/=，%=，**=，<<=，>>=，&=，^=，|=

4. python不支持自增`++`和自减`--`
5. 多重赋值

	```python
	>>> x = y = z = 1
	>>> x, y, z
	(1, 1, 1)
	```
6. 多元赋值

- 采用这种方式赋值时，等号两边的对象都是元组。

	```python
	>>> (x, y, z, w) = (1, 2.0, 'string', True)
	>>> x, y, z, w
	(1, 2.0, 'string', True)
	```
- 变量交换：利用多元赋值，无需临时变量

	```python
	>>> (x, y) = (1, 2.0)
	>>> x, y
	(1, 2.0)
	>>> (x, y) = (y, x)
	>>> x, y
	(2.0, 1)
	```

## 7. 标识符 ##

1. 合法的Python标识
	
	- 第一个字符必须是字母或下划线，不能以数字开头
	- 剩下的字符可以是由**字母、数字、下划线**组成
	- **区分大小写**
	
2. 关键字

	**and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield, None**

3. python用下划线作为变量的前缀和后缀指定特殊变量。
	
	- 单下划线开头（_xxx）:代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 `from xxx import *` 而导入；
	- 下划线开头和结尾（__xxx__）:代表 Python 里特殊方法专用的标识。

## 8. 标准数据类型

Python有五个标准的数据类型：

1. Numbers（数字）
2. String（字符串）
3. List（列表）
4. Tuple（元组）
5. Dictionary（字典）

### 1) Numbers 数字
	
1. int （有符号整型）
2. long （长整型，也可以表示成八进制和十六进制）：	
	- python长整型表达范围仅受限与用户计算机的虚拟内存总数
	- 整型与长整型逐步统一为一种整型类型，python 2.3开始不会报整型溢出错误，结果自动被转换成长整型。
3. float （浮点型）
4. complex（复数）
5. bool布尔值：特殊的整型，True 对应整型值`1`，False 对应整型值`0`。

### 2) String 字符串
	
1. 支持成对的单引号(`'...'`)，双引号(`"..."`)，三引号(`'''...'''`，`"""..."""`)来包含字符串；
2. 索引操作符`[]`和切片操作符`[:]`得到子字符串，包左不包右；
3. 索引规则：第一个字符的索引是`0`，最后一个字符索引是`-1`。
	
	```python
	>>> str='Python ' + "is " + '''cool''' + """!"""
	>>> str[-1]
	'!'
	>>> str[0:5] #包左不包右
	'Pytho'
	>>> str[1:6]
	'ython'
	>>> str[0:6]
	'Python'
	```

4. 加号`+`用于连接字符串，星号`*`用于重复字符串

	```python
	>>> 'Python ' + "is " + '''cool''' + """!"""
	'Python is cool!'
	>>> 'Python' * 2
	'PythonPython'
	```

### 3）List 列表和 Tuple 元组

1. 可以保存任意数量、任意类型、不同类型的Python对象，数字索引从`0`开始;
2. 列表用`[]`，元素的个数和值可以改变；
3. 元组用`()`，不可以更改，看成是只读的列表。
4. 切片运算得到子集 `[]`,`[:]`。

### 4）Dictionary 字典
	
1. 字典是Python中的映射数据类型，由键值对（key-value）构成;
2. 几乎所有类型的Python对象都可以用作键key，一般常用数字或字符串；
3. 值可以是任意类型的Python对象；
4. 字典元素用`{}`
	
	```python
	>>> aDict={'Key':'Value'}
	>>> aDict['Key2']='Value2'
	>>> aDict
	{'Key2': 'Value2', 'Key': 'Value'}
	>>> aDict.keys()
	['Key2', 'Key']
	>>> aDict['Key']
	'Value'
	```

## 9. 代码组 ##

- 代码块通过缩进对齐表达代码逻辑，而不是使用大括号{}。
- 代码组：缩进相同的一组语句构成一个代码块。同一代码组的代码行必须严格左对齐。
- Python对空格或者制表符都支持，但是不同文本编辑器中的制表符代表的空白宽度不一，如果代码要跨平台应用，或者被被不同编辑器编写，建议不要使用制表符。建议使用4个空格宽度。
- 没有缩进的代码块是最高层次的，被称作脚本的“主体”main部分
- 分号‘;’允许将多条语句写在同一行上，语句之间用分号隔开。（降低可读性，不建议使用）

## 10. 条件和循环语句 ##

1. 标准if语句

	```python
	if expression:  #当表达式的值非0、布尔值True时，则执行代码组if_suite。条件表达式不需要括号
		if_suite  #代码组suite是一个Python术语，由一条或多条语句组成，表示子代码块。
	```

2. if-else语句、if-elif-else语句

	```python
	if expression:
		if_suite
	else:
		else_suite
	```
	
	```python
	if expression1:
		if_suite
	elif expression2:
		elif_suite
	else:
		else_suite
	```

3. while循环语句

	```python
	while expression:
		while_suite  #循环执行到表达式的值为0或False
	```

4. for循环

- python中的for接受可迭代对象作为其参数，类似于foreach。注意：for语句的**冒号`:`**

	```python
	>>> for item in ['Python', 'is', 'cool', '!']:
		print item,  #print语句默认会给每一行添加一个换行符，添加逗号`,`可以不换行。并且在输出的元素之间自动添加一个空格
		
	Python is cool !

	>>> str='Python'
	>>> for each in str: #获取字符串每个字符
		print each,
			
	P y t h o n

	>>> for each in range(len(str)): #rang()函数和len()函数用于字符串索引
		print str[each],
	
		
	P y t h o n
	```

- Python2.3新增enumerate()函数，可同时获得字符串的索引和字符

	```python
	>>> for i, char in enumerate(str):
		print i, char
	
		
	0 P
	1 y
	2 t
	3 h
	4 o
	5 n
	```

- 内建函数range()生成数值范围内的序列

	```python
	>>> for each in range(10):
		print each,
	
		
	0 1 2 3 4 5 6 7 8 9
	```

## 11. 继续 \ ##

- 过长的语句可以使用反斜杠分解成几行。

	```python
	if (weather_is_not == 1) and \
		(shark_warnings == 0):
			send_goto_beach_mesg_to_paper()
	```

- 在使用闭合操作符 (), [], {}, 单一语句可以多行书写。（推荐使用）

	```python	
	# 给一些变量赋值
	a, b, c, d = (1,
		      'string', 20.0, -1.00)
	```

- 三引号包括下的字符串可以多行书写。
	
	```python
	>>> print '''Hi there, this is a long message
	for you that gose over multiple lines!'''

	Hi there, this is a long message
	for you that gose over multiple lines!
	``` 

## 12. 模块 ##
- 每一个Python脚本文件都可以作为一个模块；
- 模块以磁盘文件的形式存在；
- 模块里的代码可以是直接执行的脚本，也可以是类似库函数的代码，从而可以被别的模块导入使用。
- 当一个模块变得过大，并且驱动太多功能的话，应该考虑拆些代码出来另建模块。

## 13. 内存管理 ##

1. 变量名，变量类型无需事先声明。对象的类型和内存占用都是运行时确定的。
2. 变量分配内存时是在借用系统资源。Python解释器承担内存管理的任务。
3. 引用计数：追踪内存中的对象，Python使用了引用计数技术，记录所有使用中的对象有多少引用。
- 增加引用计数：
	1). 对象被创建并赋值给变量；
				
	```python 
	x=3.14 
	```
	
	2). 同一对象又被赋值给其他变量；
	
	```python 
	y = x 
	```
	
	3). 作为参数传递给函数或类实例；
	
	```python 
	funtion(x)
	```
	
	4). 成为容器对象的一个元素。
	
	```python 
	myList = [123, x, 'yz']
	```

- 减少引用计数：
	1). 引用离开其作用范围（函数运行结束，所有局部变量自动销毁）；
	2). 变量被赋值给另外一个对象时；
	
	```python 
	x=3.14
	x=123  #此时对象3.14引用计数减1
	```
	
	3). 对象的别名被显示销毁；
	
	```python 
	del x 
	```
	
	4). 对象被从一个窗口对象中移除
	
	```python 
	myList.remove(x)
	```
	
	5). 窗口对象本身被销毁
	
	```python 
	del myList 
	```

4. del语句

	del语句会删除对象的一个引用

	```python
	>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
	>>> del a[0]
	>>> a
	[1, 66.25, 333, 333, 1234.5]
	>>> del a[2:4]
	>>> a
	[1, 66.25, 1234.5]
	>>> del a[:]
	>>> a
	[]
	>>> del a
	```

5. 垃圾收集

垃圾收集器实际是一个引用计数器和一个循环垃圾收集器，用来寻找引用计数为0的对象，也负责引用计数大于0但应该被销毁的对象。