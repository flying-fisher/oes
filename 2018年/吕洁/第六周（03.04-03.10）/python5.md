# 本周主要学习了函数中参数的收集与逆过程，以及面向对象的三大特性。
# 1.参数的收集与逆过程  
为了方便用户给函数提供任意多的参数，可在参数前面加上*或**，*代表元组，**代表字典，具体实现过程如下。

输出元组：

    def print_params(*params):
        print params
    print_params(1,2,3)
    (1,2,3)

输出字典：

    def print_params1(**params):
         print params
     print_params1(x=1,y=2,z=3)
          {‘x’:1,‘y’:2,‘z’:2}
上面介绍了如何将参数收集成元组和字典，如果在参数前面再加上*和**，就可以进行相反的操作，即将元组和字典返回成参数。

在参数学习的过程中，还学习了zip函数的用法。Zip函数接受任意多个序列作为参数，返回一个turple列表，下面将介绍zip函数的几种用法。

    x=[1,2,3]
    y=[4,5,6]
    xy=zip(x,y) 
    print xy
    运行结果为：[(1,4),(2,5),(3,6)]

    x = [1, 2, 3] 
    y = [4, 5, 6, 7]
    xy = zip(x, y)
    print xy
    运行结果为：[(1,4),(2,5),(3,6)]

    x = [1, 2, 3]
    x = zip(x)
    print x
    运行结果为：[(1,),(2,),(3,)]
    
    x = zip()
    print x
    运行结果为：[]
    
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    xyz = zip(x, y, z)
    u = zip(*xyz)
    print u
    运行结果为：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    
    它的运行机制如下：
    在运行zip(*xyz)之前，xyz的值是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    那么，zip(*xyz) 等价于 zip((1, 4, 7), (2, 5, 8), (3, 6, 9))
    所以，运行结果是：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    x = [1, 2, 3]
    r = zip(* [x] * 3)
    print r
    运行结果为：[(1, 1, 1), (2, 2, 2), (3, 3, 3)]
    
    它的运行机制是这样的：
    [x]生成一个列表的列表，它只有一个元素x
    [x] *3生成一个列表的列表，它有3个元素，[x, x, x]
    zip(* [x]*3)的意思就明确了，zip(x, x, x)

# 2.面向对象的三大特性
## （1）封装

在程序设计中，封装是对具体对象的一种抽象，即将某些部分隐藏起来，在程序外部看不到，其含义是其他程序无法调用。要了解封装，离不开“私有化”，就是将类或者是函数中的某些属性限制在某个区域之内，外部无法调用。

## （2）继承
当定义一个class的时候，可以从某个现有的class继承，新的class称为子类，而被继承的class称为父类。首先编写一个名为Animal的class，有一个run()方法。

    class Animal(object):
	    def run(self)；
   		    print(‘Animal is running’)
可直接从Animal类继承，得到Dog和Cat类。

    class Dog(Animal):
	    pass
    class Cat(Animal):
	    pass
继承可以使子类获得父类的全部功能，上述例子中，Dog和Cat可使用run()方法。

    dog=Dog()
    dog.run()
    cat=Cat()
    cat.run()
    
运行结果：

    Dog is running
    Cat is running
## （3）多态

为了方便理解多态，先编写一个函数。

    def run_twice(animal)：
	    animal.run()
	    
可将Animal实例传入到函数中，即可打印出：

    run_twice(Animal())
    Animal is running
可将Dog实例传入到函数中，即可打印出：

    run_twice(Dog())
    Dog is running
可将Cat实例传入到函数中，即可打印出：

    run_twice(Cat())
    Cat is running
    
多态的好处是不需对run_twice()做任何修改，任何依赖Animal作为参数的函数和方法都可以不加修改地正常运行。对一个变量，只需知道它是Animal类型，无需确切地知道它的子类型，就可以调用run_twice()方法，由运行时参数对象的确切类型决定。这也是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；
	
对修改封闭：不需要修改依赖Animal类型的run_twice()方法。
	
### Python语言与Java语言多态的区别：
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。只需要保证传入的对象有一个run()方法就可以了。
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
