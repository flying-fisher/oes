# Python对象 #

## 1. 类型对象 ##

1. Python中类型是变量，内建函数type()返回的是类型对象。对象的一系列固有行为和特性（比如支持那些运算，具有哪些方法）必须事先定义好，类型正式保存这些信息的最佳位置。

	```python
	>>> type(888)
	<type 'int'> # 这是个类型对象
	>>> type("hello")
	<type 'str'>
	>>> type(3.14)
	<type 'float'>
	```
2. 所有类型对象的类型都是type，也是所有Python类型的根、所有Python标准类的默认元类（metaclass）。
	```python
	>>> type(type(888))
	<type 'type'>
	```

## 2. None -- Null对象 ##

Null对象或者NoneType，一个特殊的类型，只有一个值None，不支持任何运算、没有任何内建方法。

NoneType类型 类似于 void类型

NoneType的值 类似于 null值

所有标准对象均可用于布尔测试，每个对象天生具有布尔值。

下列对象的布尔值是False：
1. None
2. False
3. 所有值为0的数，整型0、浮点型0.0、长整型0L、复数0.0+0.0j、空字符串""、空列表[]、空元组()、空字典{}

## 3. 内部类型 ##

- 代码对象
- 帧对象
- 跟踪记录对象
- 切片对象

	步进切片：[起始索引：结束索引：步进值]	
	```python
	>>> string="python"
	>>> string[::-1]
	'nohtyp'
	>>> string[::-2]
	'nhy'
	>>> string[0:5:-1]
	''
	>>> string[0:5:1]
	'pytho'
	```

- 省略对象，唯一的名字是Ellipsis
- XRange对象，内建函数xrange()生成

## 3. 标准类型操作符 ##

1. 对象值的比较

	- 所有的内建类型均支持比较运算，返回布尔值。比较操作针对对象的值进行，而不是对象本身。
	
	```python
	>>> 2==2
	True
	>>> 'abc' == 'abc'
	True
	>>> 'abc' < 'xyz'
	True
	>>> [3, 'abc'] == [3, 'abc']
	True
	```
	- 多个比较操作可以在同一行进行，求值顺序从左到右

	```python
	>>> 3 < 4 < 7 #等价于(3 < 4) and (4 < 7)
	True
	>>> 3 < 4 > 7 #等价于(3 < 4) and (4 > 7)
	False
	```
2. 对象身份比较
	
作为对**值**比较的补充，python也支持**对象本身**的比较。

标准类型对象身份比较操作符：（返回值布尔类型）

```python
obj1 is obj2     #obj1 和 obj2是同一个对象
obj1 is not obj2 #obj1 和 obj2不是同一个对象
```