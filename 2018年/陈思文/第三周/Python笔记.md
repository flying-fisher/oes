# Python基础语法


### 交互式编程不需要创建脚本文件，是通过 Python 解释器的交互模式进来编写代码。


1. 在命令行中输入Python即可启动交互式编程![](https://i.imgur.com/XjX9ZyX.png)
2. Windows在安装Python时已经已经安装了默认的交互式编程客户端![](https://i.imgur.com/uSRLqWV.png)

### Python
1. Python标识符由**字母、数字、下划线**组成，但不能以数字开头。
2. 下划线开头的标识符具有特殊意义：
	
	- 单下划线开头（_name）:代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
	- 双下划线开头（__name）:代表类的私有成员;
	- 双下划线开头和结尾（__name__）:代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
3. Python标识符**区分大小写**。
4. Python可以同一行显示多条语句，方法是用**分号(;)**分开。
5. Python保留字符，不能用作常数或变数，或任何其他标识符名称。所有 Python 的关键字只包含小写字母。

	***and, exec, not, assert, finally, or, break, for, pass, class, from,	print, continue, global, raise,def, if, return, del, import, try, elif, in, while,else, is, with,except, lambda, yield***
6. Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python是用缩进来写模块。缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

	**IndentationError: unindent does not match any outer indentation level**错误表明，你使用的缩进方式不一致
7. 多行语句：使用**斜杠(\\)**将多行语句连接成一条Python语句。语句中包含 **[]**, **{}** 或 **()** 括号就不需要使用多行连接符(\\)。
8. Python可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型。其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
9. Python注释：

	- 单行注释用 # 开头 `# 第一个注释`；
	- 多行注释用三个单引号(''')或三个双引号(""")。

## 操作符

### 1. 标准算术操作符： +, -, *, /, //, %, **（指数）

优先级：**, 单目+或-, 乘除取余，加减

单斜杠 **/** ：python3.0以后，真除法，无论任何类型都会保持小数部分。

> Division (/) always returns a float

![](https://i.imgur.com/9muo0PJ.png)

双斜杠 **//** ：结果只取整数部分，若操作时是浮点型，结果是浮点型整数

> to do floor division and get an integer result (discarding any fractional result) you can use the // operator;

![](https://i.imgur.com/hDO4cMN.png)

### 2. 标准比较操作符： <, >, <=, >=, ==, !=, <>

- 返回布尔类型值：**True**, **False**
- 两种不等于：!=, <> 后者在python3.0已不可用。

### 3. 逻辑操作符：and, or, not

- 逻辑操作符可以将任意表达式连接在一起，并得到布尔值。
- A < B < C 等价与 A < B and B < C 

## Python变量赋值

### 标准数据类型

**Python有五个标准的数据类型：**

1. Numbers（数字）
2. String（字符串）
3. List（列表）
4. Tuple（元组）
5. Dictionary（字典）

**Numbers（数字）**

- int （有符号整型）
- long （长整型，也可以表示成八进制和十六进制）
- float （浮点型）
- complex（复数）


### 赋值

Python是动态类型语言，不需要预先声明变量的类型。变量的类型和值在赋值时被初始化。

1. 赋值操作符(**=**)：在python中，对象是通过**引用**传递。是将对象的引用（并不是值）赋值给变量。可以链式赋值：
    ``` python
        y=x=x+1
    ```
2. 增量赋值：算术操作符与等号组合，结果赋值给左边变量。
	
	+=，-=，*=，/=，%=，**=，<<=，>>=，&=，^=，|=