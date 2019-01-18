最近一直在写毕业论文，论文主要涉及到协同过滤推荐算法，其中用到numpy，下面简单介绍numpy的概念和使用

NumPy系统是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，
比Python自身的嵌套列表（nested list structure)结构要高效的多（该结构也可以用来表示矩阵（matrix））。

一：创建多维数组
numpy（Numerical Python）提供了python对多维数组对象的支持：ndarray，具有矢量运算能力，快速、节省空间。
numpy支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
 ndarray：N维数组对象（矩阵），所有元素必须是相同类型。 
 ndarray属性：ndim属性，表示维度个数；shape属性，表示各维度大小；dtype属性，表示数据类型。
代码如下：
import numpy;

print '使用列表生成一维数组'
data = [1,2,3,4,5,6]
x = numpy.array(data)
print x #打印数组
print x.dtype #打印数组元素的类型

print '使用列表生成二维数组'
data = [[1,2],[3,4],[5,6]]
x = numpy.array(data)
print x #打印数组
print x.ndim #打印数组的维度
print x.shape #打印数组各个维度的长度。shape是一个元组

print '使用zero/ones/empty创建数组:根据shape来创建'
x = numpy.zeros(6) #创建一维长度为6的，元素都是0一维数组
print x
x = numpy.zeros((2,3)) #创建一维长度为2，二维长度为3的二维0数组
print x
x = numpy.ones((2,3)) #创建一维长度为2，二维长度为3的二维1数组
print x
x = numpy.empty((3,3)) #创建一维长度为2，二维长度为3,未初始化的二维数组
print x

print '使用arrange生成连续元素'
print numpy.arange(6) # [0,1,2,3,4,5,] 开区间
print numpy.arange(0,6,2)  # [0, 2，4]

二：指定ndarray数组元素的类型
numpy中有很多数据类型
代码如下：
print '生成指定元素类型的数组:设置dtype属性'
x = numpy.array([1,2.6,3],dtype = numpy.int64)
print x # 元素类型为int64
print x.dtype
x = numpy.array([1,2,3],dtype = numpy.float64)
print x # 元素类型为float64
print x.dtype

print '使用astype复制数组，并转换类型'
x = numpy.array([1,2.6,3],dtype = numpy.float64)
y = x.astype(numpy.int32)
print y # [1 2 3]
print x # [ 1.   2.6  3. ]
z = y.astype(numpy.float64)
print z # [ 1.  2.  3.]

print '将字符串元素转换为数值元素'
x = numpy.array(['1','2','3'],dtype = numpy.string_)
y = x.astype(numpy.int32)
print x # ['1' '2' '3']
print y # [1 2 3] 若转换失败会抛出异常

print '使用其他数组的数据类型作为参数'
x = numpy.array([ 1., 2.6,3. ],dtype = numpy.float32);
y = numpy.arange(3,dtype=numpy.int32);
print y # [0 1 2]
print y.astype(x.dtype) # [ 0.  1.  2.]

三：ndarray的矢量化计算
矢量运算：相同大小的数组键间的运算应用在元素上 
矢量和标量运算：“广播”— 将标量“广播”到各个元素

代码如下：
print 'ndarray数组与标量/数组的运算'
x = numpy.array([1,2,3]) 
print x*2 # [2 4 6]
print x>2 # [False False  True]
y = numpy.array([3,4,5])
print x+y # [4 6 8]
print x>y # [False False False]