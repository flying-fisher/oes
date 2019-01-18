这一周主要是在了解Python的具体数据结构，因为之前学习的是java，所以就和java进行了简单比较
Python提供多种数据类型来存放数据项集合，主要包括序列（列表list和元组tuple），映射（字典dict），集合（set）
而java中则有：Collection接口，包括两大分支：List，Set； Map是一个映射接口，即key-value键值对。
Map中的每一个元素包含“一个key”和“key对应的value”。

在下面我就对这两种语言的数据类型进行比较学习，希望能够理解的更透彻一点
一 List
1：Python中的列表list

列表是一种有序的集合，相对于元组和字符串的不同是它其中的元素可变，可以随时添加和删除其中的元素。

（1） 创建list
通过list对字符串创建列表非常有效
>>> L = list("Python")
>>> L
['P', 'y', 't', 'h', 'o', 'n']

（2)访问list
根据索引来访问，注意不能越界，这一点跟数组特别像：
>>> L[0]
'P'
>>> L[-1]
'n'

（3）添加新元素
用append（）方法，把新元素追加到list的末尾；insert（）可以将一个新元素添加到特定的位置。

（4） 删除元素
删除元素可以采用pop（）方法，执行L.pop()删除list的最后一个元素，如果是特定位置的话可以采用pop（2），
2表示的是位置。
（5）替换
替换很简单，直接索引就可以。
（6）打印
>>> L = ['a','b','c']
>>> for i in L:
    print(i)   
	
2:java中的List
(1) List 是一个接口，它继承于Collection的接口。它代表着有序的队列。
(2) ArrayList, LinkedList, Vector, Stack是List的4个实现类。
　　ArrayList 是一个数组队列，相当于动态数组。它由数组实现，随机访问效率高，随机插入、随机删除效率低。
　　LinkedList 是一个双向链表。它也可以被当作堆栈、队列或双端队列进行操作。LinkedList随机访问效率低，
    但随机插入、随机删除效率低。
所以我们在使用时要根据具体需求选择List的不同实现类
具体的方法我一般是参考官方的API,说的比较详细

3：Python中的元组tuple

(1)创建
与list所不同的是，tuple一般采用（）括起来，命令行中测试
T= 1,2,3
>>> T
(1, 2, 3)
>>> T = (1,2,3)
>>> T
(1, 2, 3)
>>> T = "abc"
>>> T
'abc'
创建空元组：T = ()

（2）访问
直接索引就好，如下：
>>> T =(1,2,3)
>>> T[1]
2

（3）更改
上述定义的tuple是不变的，但是我们可以在tuple中定义list对其进行修改：
>>> T = (1,2,['a','b'])
>>> T[2][0]
'a'
>>> T[2][0] = 'c'
>>> T
(1, 2, ['c', 'b'])
在tuple中，虽然元素不可以修改，但是我们可以对其进行连接组合：
>>> T1 = [1,2,3]
>>> T2 = [4,5,6]
>>> T3 = T1 + T2
>>> T3
[1, 2, 3, 4, 5, 6]

二 映射
1：Python中的字典（dict）

映射中的每个元素都有一个专业的名字，叫做键。字典是Python中唯一内建的映射类型

（1）键类型

字典（dict）是一个存放无序的键值映射（key/value）类型数据的容器字典的键可以是数字、字符串或者是元组，
但是键必须唯一。在Python中，数字、字符串和元组都被设计成不可变类型，而常见的列表以及集合（set）都是可变的，
所以列表和集合不能作为字典的键。键可以是任何不可变类型，这正是Python中的字典最强大的地方。

（2）创建

>>> d = {}
>>> d[1] = 1
>>> d
{1: 1}
>>> d['cat'] = 'Lucy'
>>> d
{1: 1, 'cat': 'Lucy'}

（3）查找

dict是通过key来查找value，表示的是意义对应的关系，可以通过d[key]的方式来访问dict：

>>> d['cat']

'Lucy'
（4）遍历

>>> d = {}
>>> d['cat'] = 'Lucy'
>>> d['dog'] = 'Ben'
>>> for key in d:

    print(key + ":",d[key])
结果

cat: Lucy

dog: Ben

（5）优缺点

dict的第一个特点是查找速度快，而且查找的速度与元素的个数无关，而list的查找速度是随着元素的增加而逐渐下降的；
第二个特点是存储的key-value序对是没有顺序的；第三个特点是作为key得到元素是不可变的，所以list不能作为key。

dict的缺点是占用内存大，还会浪费很多内容。

2：java中的map
和Python中一样，map存放的也是键值对，其中键值不能重复
(1) Map 是映射接口，Map中存储的内容是键值对(key-value)。
(2) TreeMap内容是“有序的键值对”！
(3)HashMap的内容是“键值对，但不保证次序”！
(4) Hashtable 它继承于Dictionary(Dictionary也是键值对的接口)，而且也实现Map接口；
因此，Hashtable的内容也是“键值对，也不保证次序”。但和HashMap相比，Hashtable是线程安全的。
(5) WeakHashMap 它和HashMap的键类型不同，WeakHashMap的键是“弱键”。
其中HashMap的底层数据结构是数组加上链表的数据结构，其中使用拉链法来解决hash冲突
TreeMap 是有序的散列表，它是通过红黑树实现的。它一般用于单线程中存储有序的映射。

三 集合（set）
1：Python中的set
dict是建立了一系列的映射关系，而set是建立一系列无序的，不重复的元素。
（1）创建
创建set的方式是调用set()并传入一个list，list的元素将作为set的元素。
>>> S = set([1,2,3])
>>> S
{1, 2, 3}
重复元素在Set中自动过滤，如：
>>> S = set([1,1,2,3,4,5,4])
>>> S
{1, 2, 3, 4, 5}
（2）添加
add()添加，有重复元素可以添加，但不会有效果：
>>> S.add(4)
>>> S

{1, 2, 3, 4, 5}

>>> S.add(9)
>>> S
{1, 2, 3, 4, 5, 9}

（3）删除
>>> S.remove(9)
>>> S
{1, 2, 3, 4, 5}
（4）交集，并集
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集：
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

 2：java中的set集合
 Set的实现类都是基于Map来实现的(HashSet是通过HashMap实现的，TreeSet是通过TreeMap实现的)
(1) Set 是继承于Collection的接口。它是一个不允许有重复元素的集合。
(2) AbstractSet 是一个抽象类，它继承于AbstractCollection，AbstractCollection实现了Set中的绝大部分函数，
为Set的实现类提供了便利。
(3) HastSet 和 TreeSet 是Set的两个实现类。
        HashSet依赖于HashMap，它实际上是通过HashMap实现的。HashSet中的元素是无序的。
        TreeSet依赖于TreeMap，它实际上是通过TreeMap实现的。TreeSet中的元素是有序的。
		
四 list，tuple，dict和set的主要区别
1 .list

list是一个使用方括号括起来的有序元素集合;
List 可以作为以 0 下标开始的数组,任何一个非空 list 的第一个元素总是 L[0],
负数索引从 list 的尾部开始向前计数来存取元素。任何一个非空的 list 最后一个元素总是 L[-1];
有分片功能，两个list可以相加；append 向 list 的末尾追加单个元素；
insert 将单个元素插入到 list 中； 
extend 用来连接 list，使用一个 list 参数进行调用；
append 接受一个参数, 这个参数可以是任何数据类型, 并且简单地追加到 list 的尾部；
index 在 list 中查找一个值的首次出现并返回索引值；
要测试一个值是否在 list 内, 使用 in, 如果值存在, 它返回 True, 否则返为 False ；
remove 从 list 中删除一个值的首次出现；
pop 可以删除 list 的最后一个元素, 然后返回删除元素的值，用索引删除制定位置的值；
 
2.tuple
tuple是不可变的list，创建了一个tuple就不能以任何方式改变它；
定义tuple是将整个元素集是用小括号括起来，是有序集合；
tuple的索引与list一样从0开始,所以一个非空的tuple的第一个元素总是t[0]；
负数索引与 list 一样从 tuple 的尾部开始计数；
与 list 一样分片 (slice) 也可以使用。分割一个 tuple 时, 会得到一个新的 tuple；
没有 append、extend、remove或pop方法以及index方法；
可以使用in来查看一个元素是否存在于tuple 中。

3.dict
dict定义了键和值之间的一一对应关系，每个元素都是一个key-value对；
整个元素集合用大括号括起来，有序集合；
可以通过 key 得到value, 但不能通过vaule获取 key；
在一个 dict中不能有重复的 key, 并且 key 是大小写敏感的；
键可以是数字、字符串或者是元组等不可变类型；
用del使用key可以删除dict中的独立元素； 
用clear可以清除dict中的所有元素。

4.set
set是建立一系列无序的，不重复的元素；
创建set的方式是调用set()并传入一个list，list的元素将作为set的元素；
set和dict的唯一区别仅在于没有存储对应的value。