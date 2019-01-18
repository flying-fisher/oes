# Python 内置类型

Python解释器内置的类型

包括：numerics、sequences、mappings、classes、instances 和 exceptions

一些可变的集合类，在进行加减等操作时，不会返回对象自身

所有对象都可以进行比较、真值测试、字符串转化（repr()或str()）

## 1. 真值测试

- 所有对象都可进行真值测试
- 用于if、while或布尔运算
- 与类的\_\_bool\_\_()、\_\_len()\_\_返回值有关，false的对象包括：
  - None与False
  - 数字：0，0.0，0j，Decimal(0)，Fraction(0,1)
  - 序列和集合：''，()，[]，{}，set()，range(0)


## 2. 布尔运算

- and，or，not
- and，or总是返回其中一个操作数

## 3. 比较运算

- 8个
- 除了数值型，任何不同类型的对象都不会相等
- 不同类型对象不能比较大小
- 同一类型对象的比较，与其\_\_eq\_\_()方法有关
- 对象的排序，与其\_\_lt\_\_()，\_\_le\_\_()，\_\_gt\_\_()，\_\_ge\_\_()等方法有关
- is和is not运算不能自定义，可以用于任意两个对象，不会抛异常
- in和not in只适用于序列对象的

## 4. 数值类型

- 主要3种：整型int，浮点型 float，复数型complex
- 布尔类型是整型的子类型
- 整型精度无限，浮点型使用C的double实现，sys.float_info可以查看具体信息
- 复数型包含实部real和虚部imaginary
- 还包含：分数型fractions，存储有理数；小数型decimal，存储自定义精度的浮点数



- 数值类型通过数字字面量、内建函数或运算符得到
  - 未修饰的整数字面量，包括二进制、八进制、十进制和十六进制，生成整型数值
  - 加了小数点或幂指数的字面量，生成浮点型数值
  - 把'j'或'J'附到数字后面，生成虚部数值
  - int()，float()，complex()为构造函数



- Python支持混合运算，在进行运算或比较时，小范围的数值会转换为大范围的数值	

- 运算

  ```python
  x + y
  x - y
  x * y
  x / y	# 除
  x // y	# 整除 math.floor(x/y)
  divmod(x,y)
  x % y	# 模
  x ** y 	# 乘方
  pow(x,y)
  abs(x)
  int(x)
  float(x)
  complex(re,im)
  c.conjugate() # 共轭复数
  ```

  ```python
  math.trunc(x)
  math.floor(x)
  math.ceil(x)
  round(x[,n])
  ```

### 4.1 整型的位运算


- 仅用于整型
- 优先级：数值运算>=位运算>比较


### 4.2 整型的方法

- int类实现了numbers.Integral抽象类，还提供了以下方法：
  - int.bit_length() 返回二进制长度
  - int.to_bytes(*length, byteorder, \*, signed=False*)  返回表示整数的字节
  - *classmethod* int.from_bytes(*bytes, byteorder, \*, signed=False*)  返回整型数值


### 4.3 浮点型的方法

- float类实现了numbers.Real抽象类，还提供了以下方法：
  - float.as_integer_ratio()
  - float.is_integer()
  - float.hex()

### 4.4 数值类型的哈希

- 对于不同类型的数值x、y，当x==y时，需要hash(x)\==hash(y)，对于所有的数值类型，Pyhton的hash方法是一个适用于任何有理数的数学函数，具体见sys.hash_info
- 素数P=2*\*31-1或2\*\*61-1
- x=m/n为非负有理数，且n不能被P整除时，hash(x)被定义为m * invmod(n, P) % P
- ...

## 5. Iterator迭代器类型

- Python支持在容器中迭代的概念，通过两种不同的方法实现，用于用户自定义支持迭代的类型

- 为容器实现container.\_\_iter\_\_()方法，使其支持迭代。该方法返回一个iterator object迭代器对象，该对象支持下述迭代器协议

- 迭代器iterator对象需要支持如下两个方法：
  - iterator.\_\_iter\_\_()：返回迭代器对象本身
  - iterator.\_\_next\_\_()：返回来自容器的下一个元素，如果没有则抛StopIteration异常

- Python为不同的序列类型定义了几种迭代器对象，其核心均是实现上述的迭代器协议

- 当next方法抛出StopIteration异常时，必须在后续调用中继续这样做

  ​

> Python中 list，truple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？
>
> 因为和迭代器相比有一个很大的不同，list/truple/map/dict这些数据的大小是确定的，也就是说有多少事可知的。但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。
>
> 集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但可通过iter()函数获得一个Iterator对象

**判断是否为迭代器 Iterator**

```python
from collections import Iterator  
isinstance({}, Iterator)  # False  
isinstance((), Iterator) # False  
isinstance( (x for x in range(10)), Iterator)  # True  
```

**判断是否可以迭代 Iterable**

```python
from collections import Iterable  
isinstance({}, Iterable) # True  
isinstance((), Iterable) # True  
isinstance(100, Iterable) # False  
```



```python
#for
for x in [1,2,3,4,5]:  
    pass  

#iterator  
it = iter([1,2,3,4,5])  
while True:  
    try:  
        x = next(it);  
    except StopIteration:  
        break
```



### 5.1 Generator生成器类型

- Generator生成器提供了实现迭代器协议的便利方法
- 容器对象的container.\_\_iter\_\_()方法实现为生成器，会返回一个iterator对象（也是generator对象）

## 6 序列类型 - list，tuple，range

- 如标题所示的三种基本的序列类型
- 还有定制的序列类型，用于处理二进制数据和文本字符串

### 6.1 常见序列操作

- **下列操作适用于大部分序列类型，包括可变和不可变序列**

  - x in s

  - x not in s

    - 同样适用于str，bytes和bytearray特殊序列的子串检测

  - s + t 将s和t连接在一起

    - 连接不可变序列时，得到一个新对象，所以，通过++++创建序列将带来与序列长度相关的平方时间复杂度
    - 想要得到线性的时间复杂度：
      1. 对于str序列对象，先创建list，再用str.join()或io.StringIO
      2. 对于bytes序列对象，类似于1.，或用可变序列bytearray，这个拥有高效的分配机制
      3. 对于tuple对象，先使用list
      4. 对于其他对象，参考相关类文档

  - s\*n  或  n\*s 等于将s序列重复n次

    - n = 0 时，得到空序列

    - 元素并非复制，而是***被引用了n次***

      ```python
      >>> lists = [[]] * 3
      >>> lists
      [[], [], []]
      >>> lists[0].append(3)
      >>> lists
      [[3], [3], [3]]
      >>> id(lists[0])
      2067409507144
      >>> id(lists[1])
      2067409507144
      >>> id(lists[2])
      2067409507144
      ```

    - 一些序列只支持特殊模式的元素序列，不适用于+和*，如range

  - s[i]

  - s[i:j]

  - s[i:j:k] 得到s的切片，从i到j，步长为k

    - i，j是负数则从后向前数，最后一个是-1
    - [i, j)区间，超出范围得到的都是空序列
    - i缺省为0，j缺省为len(s)
    - i，i+k，i+2*k...

  - len(s)

  - min(s)

  - max(s)

  - s.index(x[, i[, j]])

    - s.index('h',2,5)返回'h'元素在2到5范围内第一次出现的位置
    - 约等于s[2:5].index('h')，只是不会做切片，且返回的是在原序列的索引，而非切片的索引
    - 没找到抛ValueError错误

### 6.2 不可变序列类型

- 支持hash()，使得tuple等不可变序列可用于dict的key或set

### 6.3 可变序列类型

- 可变序列类型支持的操作：

  - s[i] = x

  - x[i:j] = t 以**可迭代的t对象**去替换x的i到j部分

    ```python
    >>> l=[1,2,3,4,5,6]
    >>> l[1:]='hello'
    >>> l
    [1, 'h', 'e', 'l', 'l', 'o']
    >>> l[2:] = 1 # 不能迭代
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only assign an iterable
    >>> l[2:] = [1] # 只够迭代一下
    >>> l
    [1, 'h', 1]
    >>> l[2:] = [] # 一下都没迭代
    >>> l
    [1, 'h']
    ```
    ```python
    >>> from collections import Iterable # 载入模块
    >>> isinstance('abc',Iterable) # 字符串是可迭代对象吗？
    True
    >>> isinstance([1,2,3],Iterable) # list是可迭代对象吗？
    True
    >>> isinstance({'dede':123},Iterable) # 字典是可迭代对象吗？
    True

    from collections import Iterable  
    isinstance({}, Iterable) # True  
    isinstance((), Iterable) # True  
    isinstance(100, Iterable) # False  
    ```
    http://blog.csdn.net/ducklikejava/article/details/73612631

  - s[i:j:k] = t 这里的t不仅要可迭代，还要同切片长度一致

    ```python
    >>> l=[1,2,3,4,5,6]
    >>> l[::2] = 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must assign iterable to extended slice
    >>> l[::2] = [0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: attempt to assign sequence of size 1 to extended slice of size 3
    >>> l[::2] = '000'
    >>> l
    ['0', 2, '0', 4, '0', 6]
    ```

  - del s[i:j] 等同于 s[i:j] = [] 可以看成迭代，也可以看出remove

  - del s[i:j:k] 等同于remove 切片元素，**切片是浅拷贝**

  - s.append(x) 等同于s[len(s):len(s)] = [x]

  - s.clear() 等同于del s[:]

  - s.copy() **浅拷贝**

    - www.cnblogs.com/wilber2013/p/4645353.html
    - dict和set不支持切片，所以用clear和copy保证序列接口的一致性

  - s.extend(t) 或 s += t

  - s*=n  n可以是整数或实现了\_\_index\_\_()方法的对象

  - s.insert(i,x)

  - s.pop([i])

  - s.remove(x) 移除等于x的元素，没有则ValueError

  - s.reverse()

### 6.4 Lists

- 可变序列，用于存储不同质元素
- ​


- 创建list的有如下：
  - [], [a], [a, b, c]
  - 列表推导式：[x for x in iterable]
  - 类构造器：list()或list(iterable)
    - iterable可以是序列、支持迭代的容器或迭代器对	象
    - iterable是list的话，相当于copy和iterable[:]
- 一些操作会产生list，如内建的sorted()
- list除了实现上两个小节的方法外，还包括sort()
  - 使用<进行元素的比较，比较出错的话会中断sort
  - sort()的两个参数为keyword-only arguments
    - key = str.lower
    - reverse = False

### 6.5 Tuples

- 不可变序列，用于存储
- 创建tuple有如下方式：
  - ()，a, 或(a,)，a,b,c或(a,b,c)
  - 构造函数tuple()或tuple(iterable)
    - iterable是tuple的话，返回自身，不同于list

### 6.6 Ranges

- range类型为不可变序列，通常用于for中循环特定次数
- range(stop)或range(start,stop[,step])
  - 参数为integers（int或实现了\_\_index\_\_() 的类型）
  - start没有的话，为0，step没有的话，为1
  - step为非0整数
- range类实现了除连接和重复外的所有不可变序列方法。因为range类型只用于代表严格遵循range公式的序列，连接和重复会破坏该规则
- range类型相对于list和tuple的优点在于：
  - range类型只需存3个值，占用固定的很小的内存空间
- range类实现collections.abc.Sequence，提供判断存在、查看索引、切片、负索引等操作
- range可使用==和!=比较

## 7. 文本序列类型 - str

- 文本数据在Python中使用str或string类型操作
- 使用unicode的不可变序列
- 多种写法：
  - 单引号，可嵌入双引号
  - 双引号，可嵌入单引号
  - 三单/双引号，可跨越多行，包含空格，行间以\n连接
- 多个str间仅以空格间隔，等同于一个str
- r前缀使得str不转义，u前缀好像在Python2和3中功能不同
- 虽然str是不可变序列，通过str.join()或io.StringIO可以通过多个片段高效地构建str
- str(object)
  - object缺省时，返回空字符串
  - 具体规则根据encoding和errors参数而定

### 7.1 String的方法

- 除了基本的序列操作外（in，not in，+，*，切片等），还有好多str的方法
- str有两种格式化方式：
  - str.format()
  - 类似于c的printf

str的方法，太多了

- str.capitalize()——copy，并首字母大写
- str.casefold()——copy，并全部小写（有点区别）
- str.center(width[,fillchar])
- str.count(sub[,start[,end]])——统计sub出现的次数
- str.encode(encoding="utf-8",errors="strict")
- ...太多了

### 7.2 printf式的字符串格式化{#7.2}

str类型支持一个内建操作%，用于格式化字符串：
- format % values
- values为单个对象或tuple类型或dict类型
- format中的转换说明符
  - 至少两个字符，具体如下述
  - % 带头
  - mapping key（可选），对应dict类型value的key
  - 转换标志（可选）—— #,0,-.....
  - 最小宽度（可选）
  - 精度（可选），以小数点开头
  - 长度修改（可选）
  - 转换类型 —— d,s,f

## 8. 二进制序列类型 - bytes，bytearray，memoryview

- bytes和bytearray用于操作二进制数据，memoryview用于访问二进制数据的内存，而无需进行copy
- array module支持对基本数据的高效存储

### 8.1 Bytes类型

- 不可变序列
- 提供一些仅支持ASCII数据的方法
- 语法同str类型相似，只是增加了b前缀，只支持ASCII字符
- 也可以使用r前缀使得序列不转义
- 因为是以ASCII字符为基础的，所以bytes对象实际上和不可变的整数序列相似，序列中的每个值0<=x<256。
- 虽然很多二进制数据包含ASCII字符，可以使用文本处理算法，但可能导致数据损坏。最好在bytes类型上使用。
- 创建bytes对象的方法：
  - bytes(10)——固定长度，以0填充
  - bytes(range(20))——iterable
  - bytes(obj)——复制对象的二进制数据
- 类方法：fromhex(string)
- hex()

### 8.2 Bytearray对象

- Bytes对象对应的可变序列
- 类方法：fromhex(string)
- hex()

### 8.3 Bytes和Bytearray的操作

- 常见的序列操作同时适用于可变和不可变序列，即（in，not in，+，*，切片等）适用于Bytes和Bytearray
- 适用于ASCII的操作
- 以下操作适用于任意二进制数据，bytes的，bytearray的
  - 大概有count，decode
  - startswith，endswith
  - find，rfind
  - index，rindex
  - partition，rpartition
  - lstrip，rstrip，strip
  - split，rspilt
  - join，maketrans，replace，center等等太多了

### 8.4 printf式bytes格式化

- 好像和[7.2小节](#7.2)差不多，具体没看

### 8.5 memoryview类型

- 无需copy，访问obj的内存数据，obj需支持buffer协议
- 好像和内存模型关系密切，具体待研究

## 9. 集合类型 - set，frozenset

- 无序，不同hash值的对象集合
- common uses 包括：判断是否包含，序列去重，集合的运算
- 由于无序，不支持索引、切片等操作
- set是可变的，没有hash值
- frozenset为不可变的，可以hash，因此可用作于dict的key，也可作为set的元素
- 创建方法：
  - set：{}，{'123'}，{'123',123}
  - set()，frozenset()
- 元素要hashable
- 提供的操作：
  - len()
  - in，not in
  - isdisjoint()，issubset()，issuperset()
  - union()，intersection()
  - difference()，symmetric_difference()
  - 注意非运算符的方法，与运算符使用上的区别
- set和frozenset都支持比较，注意空集合的比较
- 可变集合set还有一些方法：
  - add()，remove()，clear()——如果没有，删除时KeyError
  - discard()——如果有某元素，则删除
  - pop()——弹出任意元素，空集合时KeyError

## 10. Mapping类型 - dict

- ”将可hash的值映射到任意对象“

- 可变类型

- key-value：

  - hashable的对象可以作为key

  - 数值类型也可作为key，以数值比较作为规则（1==1.0）

    ```python
    >>> di = {1:1,1.1:1}
    >>> type(di)
    <class 'dict'>
    >>> di = {1:1,1.00:1}
    >>> di
    {1: 1}
    ```

  - value可以是不能hash的，如list，dict等可变类型（这些类型的比较是基于元素的而非对象自身）

- 创建dict：

  ```python
  >>> a = dict(one=1, two=2, three=3)
  >>> b = {'one': 1, 'two': 2, 'three': 3}
  >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
  >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
  >>> e = dict({'three': 3, 'one': 1, 'two': 2})
  >>> a == b == c == d == e
  True

  ```

- mapping类型支持的方法：

  - 多

### 10.1 dict view 对象

- dict.key()，dict.values()，dict.item()返回的对象

- 是对dict的动态view，即会随着dict的改变而改变

- 支持迭代，以及存在性判断

  - len(dictview)
  - iter(dictview)
  - x in dictview

  ```python
  >>> d={'python':1,'php':2,'java':3}

  #默认迭代的是key
  >>> for i in d:
      print(i)
  python
  php
  java

  #dictview
  #迭代key
  >>> for key in d.keys():
      print(key)
  python
  php
  java

  #迭代value
  >>> for value in d.values():
      print(value)
  1
  2
  3

  #同时迭代key,value
  >>> for k , v in d.items():
      print(k,v)
  python 1
  php 2
  java 3
  ```

  ```python
  #对于一个列表，迭代其下标
  l=['python','php','java','c++']
  #第一种
  for x in range(len(l)):
      print(x,l[x])
  #第二种
  for i ,value in enumerate(l):
      print(i,value)
  #运行结果
  0 python
  1 php
  2 java
  3 c++
  #在同一行输出：
  for i ,value in enumerate(l):
      print(i,value ,end=',')
  #运行结果
  0 python,1 php,2 java,3 c++,
  ```

  ​

## 11. 上下文管理类型

- 和with statement有关

## 12. 其他内置类型

- Python解释器还有其他一些内置类型，




































