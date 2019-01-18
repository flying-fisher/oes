# Python内建函数

## 数学运算

- abs(*x*)——返回int、float的绝对值，返回complex的模

  ```python
  >>> abs(-1.5)
  1.5
  >>> abs(3+4j)
  5.0
  ```

- divmod(*a*,*b*)——返回两数的商和余数

  ```python
  >>> divmod(5,2)
  (2, 1)
  >>> divmod(5.5,2) #math.floor(5.5/2)
  (2.0, 1.5)
  ```

- max(*iterable*, \*[, *key*, *default*])

- max(*arg1*, *arg2*, \**args*[, *key*])——返回iterable或多个数中的最大值，强制关键字参数key为one-argument ordering function

- ```python
  >>> max('1234') # 传入1个可迭代对象，取其最大元素值
  '4'
  >>> max(-1,0) # 数值默认去数值较大者
  0
  >>> max(-1,0,key = abs) # 传入了求绝对值函数，则参数都会进行求绝对值后再取较大者
  -1
  ```

- min(*iterable*, \*[, *key*, *default*])

- min(*arg1*, *arg2*, \**args*[, *key*])——返回iterable或多个数中的最小值
  ```python
  >>> min('1234') # 传入1个可迭代对象，取其最小元素值
  '1'
  >>> min(-1,-2) # 数值默认去数值较小者
  -2
  >>> min(-1,-2,key = abs)  # 传入了求绝对值函数，则参数都会进行求绝对值后再取较小者
  -1
  ```

- pow(*x*, *y*[, *z*]) ——幂运算结果或幂运算再与z求模
- ```python
  >>> pow(2,3)
  8
  >>> pow(2,3,5)
  3
  ```

- round(*number*[, *ndigits*])——取最近的整数
  ```python
  >>> round(1.1314926,1)
  1.1
  >>> round(1.1314926,5)
  1.13149
  #小数部分为0.5时，取最近的偶数
  >>> round(0.5)
  0
  >>> round(1.5)
  2
  >>> round(2.5)
  2
  ```

- sum(*iterable*[, *start*])——对iterable对象的元素求和
  ```python
  >>> sum((1,2,3,4))
  10
  >>> sum((1.5,2.5,3.5,4.5))
  12.0
  >>> sum((1,2,3,4),-10) #起始值-10
  0
  ```


## 类型转换

- *class* bool([*x*])——根据x的truth testing procedure返回布尔值	

  ```python
  >>> bool() #未传入参数
  False
  >>> bool(0) #数值0、空序列等值为False
  False
  >>> bool(1)
  True
  ```

- *class* int([*x*])——根据x返回整数值，

  ```python
  >>> int() #不传入参数时，得到结果0。
  0
  >>> int(-3.1)
  -3
  >>> int(3.6)
  3
  ```

- ord()，chr()——Unicode字符与对应整数间的转换

  ```python
  >>> ord('a')
  97
  >>> chr(97)
  'a'
  ```

- bin(*x*)，oct(*x*)，hex(*x*)——将整数转化成不同进制的字符串

  ```python
  >>> bin(3) 
  '0b11'
  >>> oct(10)
  '0o12'
  >>> hex(15)
  '0xf'
  ```

- *class* float([*x*])——根据x返回浮点数

  ```python
  >>> float() #不提供参数的时候，返回0.0
  0.0
  >>> float(3)
  3.0
  >>> float('3')
  3.0
  ```

- *class* complex([*real*[, *imag*]])——构造复数


- *class* list([*iterable*])——根据iterable构造list对象
  ```python
  >>>list() # 不传入参数，创建空列表
  [] 
  >>> list('abcd') # 传入可迭代对象，使用其元素创建新的列表
  ['a', 'b', 'c', 'd']
  ```

- tuple([*iterable*])——根据iterable得到tuple对象
  ```python
  >>> tuple() #不传入参数，创建空元组
  ()
  >>> tuple('121') #传入可迭代对象。使用其元素创建新的元组
  ('1', '2', '1')
  ```

- range(*stop*)，range(*start*, *stop*[, *step*])——返回range对象
  ```python
  >>> a = range(10)
  >>> b = range(1,10)
  >>> c = range(1,10,3)
  >>> a,b,c # 分别输出a,b,c
  (range(0, 10), range(1, 10), range(1, 10, 3))
  >>> list(a),list(b),list(c) # 分别输出a,b,c的元素
  ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 4, 7])
  ```

- *class* slice(*stop*)，*class* slice(*start*, *stop*[, *step*])——构造切片对象

- *class* str(*object=''*)，*class* str(*object=b''*, *encoding='utf-8'*, *errors='strict'*)——构造str对象
  ```python
  >>> str()
  ''
  >>> str(None)
  'None'
  >>> str('abc')
  'abc'
  >>> str(123)
  '123'
  ```

- *class* bytearray([*source*[, *encoding*[, *errors*]]])——构造bytearray对象，[0,255]范围的整数组成的可变序列
  ```python
  >>> bytearray('中文','utf-8')
  bytearray(b'\xe4\xb8\xad\xe6\x96\x87')
  ```

- *class* bytes([*source*[, *encoding*[, *errors*]]])——构造bytes对象，[0,255]范围的整数组成的不可变序列
  ```python
  >>> bytes('中文','utf-8')
  b'\xe4\xb8\xad\xe6\x96\x87'
  ```

- *class* set([*iterable*])——根据iterable构造set对象

- *class* frozenset([*iterable*])——根据iterable构造frozenset对象，不可变，hashable

- *class* dict(*\*\*kwarg*)，*class* dict(*mapping*,*\*\*kwarg*)，*class* dict(*iterable*,*\*\*kwarg*)——dict类型构造函数

    ```python
    >>> dict() # 不传入任何参数时，返回空字典。
    >>>   {}
    >>> dict(a = 1,b = 2) #  可以传入键值对创建字典。
    >>>   {'b': 2, 'a': 1}
    >>> dict(zip(['a','b'],[1,2])) # 可以传入映射函数创建字典。
    >>>   {'b': 2, 'a': 1}
    >>> dict((('a',1),('b',2))) # 可以传入可迭代对象创建字典。
    >>>   {'b': 2, 'a': 1}
    ```

- enumerate(*iterable*, *start=0*)——返回枚举对象

    ```python
    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    >>>   [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1)) #指定起始值
    >>>   [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    ```

- iter(*object*[, *sentinel*])——返回迭代器iterator对象

    ```python
    >>> a = iter('abcd') #字符串序列
    >>> a
    >>>   <str_iterator object at 0x03FB4FB0>
    >>> next(a)
    >>>   'a'
    >>> next(a)
    >>>   'b'
    >>> next(a)
    >>>   'c'
    >>> next(a)
    >>>   'd'
    >>> next(a)
    >>>   Traceback (most recent call last):
      File "<pyshell#29>", line 1, in <module>
        next(a)
    StopIteration
    ```

## 可迭代对象操作

- all(*iterable*)——iterable是否全为True
- any(*iterable*)——iterable是否包含True
- filter(*function*, *iterable*)——使用指定方法过滤iterable对象，返回一个iterator
- map(*function*, *iterable*)——使用指定方法对iterable对象进行映射，返回一个iterator
- next(*iterator*[, *default*])——通过调用迭代器iterator的\_\_next\_\_()方法，取出下一个元素
- reversed(*seq*)——返回序列反转后对应的迭代器iterator
- sored(*iterable*, ***, *key=None*, *reverse=False*)——返回iterable对象中元素排序后的list
- zip(*\*iterables*)——返回多个iterable对象聚合成的迭代器iterator

## 对象操作

- help([*object*])——查看内建函数或类型的帮助信息

    ```python
    >>> help(str)
    Help on class str in module builtins:

    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, returns the result of object.__str__() (if defined)
     |  or repr(object).
     |  encoding defaults to sys.getdefaultencoding().
     |  errors defaults to 'strict'.
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __format__(...)
     |      S.__format__(format_spec) -> str
     |
     |      Return a formatted version of S as described by format_spec.
    -- More  --
    ```

- dir([*object*])——返回当前作用域或对象的属性列表

    ```python
    >>> dir(list('123'))
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    ```

- *class* type(*object*)，*class* type(*name*, *bases*, *dict*)——返回对象的类型，或根据传入参数创建一个新类型

- id(*object*)——返回对象的标识符，该标识符在对象的生命周期内唯一且不变

- hash(*object*)——返回对象的hash值

  ```python
  >>> hash((1,2,3,4,5))
  8315274433719620810
  >>> hash({1,2,3,4,5})
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: unhashable type: 'set'
  >>> hash(frozenset((1,2,3,4,5)))
  4645684509812374175
  ```

- len(*s*)——返回序列或集合对象的长度

- ascii(*object*)——返回对象的可打印表字符串表现方式

- format(*value*[, *format_spec*])——格式化显示

- vars([*object*]) ——返回当前作用域内的局部变量和其值组成的字典，或者返回对象的属性列表

    ```python
    #作用于类实例
    >>> class A(object):
        pass
    >>> a = A()
    >>> a.__dict__
    {}
    >>> vars(a)
    {}
    >>> a.name = 'Kim'
    >>> a.__dict__
    {'name': 'Kim'}
    >>> vars(a)
    {'name': 'Kim'}
    ```

## 反射操作

- \_\_import\_\_(*name*, *globals=None*, *locals=None*, *fromlist=()*, *level=0*) ——动态导入模块

- isinstance(*object*, *classinfo*) ——判断是否是类或者类型元组中任意类元素的实例

  ```python
  >>> isinstance(1,int)
  True
  >>> isinstance(1,str)
  False
  >>> isinstance(1,(int,str))
  True
  ```

- issubclass(*class*, *classinfo*) ——判断是否是类或者类型元组中任意类元素的子类
  ```python
  >>> issubclass(bool,int)
  True
  >>> issubclass(bool,str)
  False
  >>> issubclass(bool,(str,int))
  True
  ```
- hasattr(*object*, *name*)——判断对象是否有某一属性

- getattr(*object*, *name*)，setattr(*object*, *name*)，delattr(*object*, *name*)——获取/设置/删除对象的某一属性值

- callable(*object*) ——判断对象是否可以被调用，对象的类如果有\_\_call\_\_()方法即可被调用

## 变量操作

- locals()——返回当前作用域内的局部变量和其值组成的字典

    ```python
    >>> def f():
        print('before define a ')
        print(locals()) #作用域内无变量
        a = 1
        print('after define a')
        print(locals()) #作用域内有一个a变量，值为1

    >>> f()
    before define a 
    {} 
    after define a
    {'a': 1}
    ```

- globals()——返回当前作用域内的全局变量和其值组成的字典


## 交互操作

- print(**objects*, *sep=' '*, *end='\n'*, *file=sys.stdout*, *flush=False*)——向file打印输出
- input([*prompt*])——读取输入

## 文件操作

- open(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)——使用指定的模式和编码打开文件，返回相应的文件读写对象
