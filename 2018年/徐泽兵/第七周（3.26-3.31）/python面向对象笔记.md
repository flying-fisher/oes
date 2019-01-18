抽象是隐藏多余细节的艺术。在面向对象的概念中，抽象的直接表现形式通常为类。虽然Python是解释性语言，但是它是面向对象的，从设计之初就已经是一门面向对象的语言。 Python基本上提供了面向对象编程语言的所有元素，如果你已经至少掌握了一门面向对象语言，那么利用Python进行面向对象程序设计将会相当容易。 下面就来了解一下如何在Python中进行对象编程。

一. 如何定义一个类

　　在进行python面向对象编程之前，先来了解几个术语：类，类对象，实例对象，属性，函数和方法。

　　类是对现实世界中一些事物的封装，定义一个类可以采用下面的方式来定义：

class className:
block

注意类名后面有个冒号，在block块里面就可以定义属性和方法了。当一个类定义完之后，就产生了一个类对象。类对象支持两种操作：引用和实例化。引用操作是通过类对象去调用类中的属性或者方法，而实例化是产生出一个类对象的实例，称作实例对象。比如定义了一个people类：

class people:
name = 'jack' #定义了一个属性

#定义了一个方法  
def printName(self):  
    print self.name  
　　people类定义完成之后就产生了一个全局的类对象，可以通过类对象来访问类中的属性和方法了。当通过people.name（至于为什么可以直接这样访问属性后面再解释，这里只要理解类对象这个概念就行了）来访问时，people.name中的people称为类对象，这点和C++中的有所不同。当然还可以进行实例化操作，p=people( )，这样就产生了一个people的实例对象，此时也可以通过实例对象p来访问属性或者方法了(p.name).

　　理解了类、类对象和实例对象的区别之后，我们来了解一下Python中属性、方法和函数的区别。

　　在上面代码中注释的很清楚了，name是一个属性，printName( )是一个方法，与某个对象进行绑定的函数称作为方法。一般在类里面定义的函数与类对象或者实例对象绑定了，所以称作为方法；而在类外定义的函数一般没有同对象进行绑定，就称为函数。

二. 属性

　　在类中我们可以定义一些属性，比如：

class people:
name = 'jack'
age = 12

p = people()
print p.name,p.age
　　定义了一个people类，里面定义了name和age属性，默认值分别为'jack'和12。在定义了类之后，就可以用来产生实例化对象了，这句p = people( )实例化了一个对象p，然后就可以通过p来读取属性了。这里的name和age都是公有的，可以直接在类外通过对象名访问，如果想定义成私有的，则需在前面加2个下划线 ' __'。

class people:
name = 'jack' age = 12

p = people()
print p.name,p.age
　　这段程序运行会报错： Traceback (most recent call last):
File "C:/PycharmProjects/FirstProject/oop.py", line 6, in 
print p.name,p.age
AttributeError: people instance has no attribute 'name
　　提示找不到该属性，因为私有属性是不能够在类外通过对象名来进行访问的。在Python中没有像C++中public和private这些关键字来区别公有属性和私有属性，它是以属性命名方式来区分，如果在属性名前面加了2个下划线''，则表明该属性是私有属性，否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

三. 方法

　　在类中可以根据需要定义一些方法，定义方法采用def关键字，在类中定义的方法至少会有一个参数，，一般以名为'self'的变量作为该参数（用其他名称也可以），而且需要作为第一个参数。下面看个例子：

class people:
name = 'jack' age = 12

def getName(self):  
    return self.__name  
def getAge(self):  
    return self.__age  
p = people()
print p.getName(),p.getAge()
　　如果对self不好理解的话，可以把它当做C++中类里面的this指针一样理解，就是对象自身的意思，在用某个对象调用该方法时，就将该对象作为第一个参数传递给self。

四. 类中内置的方法

　　在Python中有一些内置的方法，这些方法命名都有比较特殊的地方（其方法名以2个下划线开始然后以2个下划线结束）。类中最常用的就是构造方法和析构方法。

　　构造方法init(self,....)：在生成对象时调用，可以用来进行一些初始化操作，不需要显示去调用，系统会默认去执行。构造方法支持重载，如果用户自己没有重新定义构造方法，系统就自动执行默认的构造方法。

　　析构方法del(self)：在释放对象时调用，支持重载，可以在里面进行一些释放资源的操作，不需要显示调用。

　　还有其他的一些内置方法，比如 cmp( ), len( )等。下面是常用的内置方法：

内置方法 说明 init(self,...) 初始化对象，在创建新对象时调用 del(self) 释放对象，在对象被删除之前调用 new(cls,args,**kwd) 实例的生成操作 str(self) 在使用print语句时被调用 getitem(self,key) 获取序列的索引key对应的值，等价于seq[key] len(self) 在调用内联函数len()时被调用 cmp(stc,dst) 比较两个对象src和dst getattr(s,name) 获取属性的值 setattr(s,name,value) 设置属性的值 delattr(s,name) 删除name属性 getattribute() getattribute()功能与getattr()类似 gt(self,other) 判断self对象是否大于other对象 lt(slef,other) 判断self对象是否小于other对象 ge(slef,other) 判断self对象是否大于或者等于other对象 le(slef,other) 判断self对象是否小于或者等于other对象 eq(slef,other) 判断self对象是否等于other对象 call(self,args) 把实例对象作为函数调用　　init():init方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希望的初始化。注意，这个名称的开始和结尾都是双下划线。代码例子:

Filename: class_init.py
class Person:
def init(self, name):
self.name = name
def sayHi(self):
print 'Hello, my name is', self.name

p = Person('Swaroop')
p.sayHi()

输出：
Hello, my name is Swaroop
　　new():new()在init()之前被调用，用于生成实例对象。利用这个方法和类属性的特性可以实现设计模式中的单例模式。单例模式是指创建唯一对象吗，单例模式设计的类只能实例化一个对象。

class Singleton(object):
__instance = None # 定义实例

def __init__(self):  
    pass  

def __new__(cls, *args, **kwd):         # 在__init__之前调用  
    if Singleton.__instance is None:    # 生成唯一实例  
        Singleton.__instance = object.__new__(cls, *args, **kwd)  
    return Singleton.__instance  
　　getattr()、setattr()和getattribute():当读取对象的某个属性时，python会自动调用getattr()方法。例如，fruit.color将转换为fruit.getattr(color)。当使用赋值语句对属性进行设置时，python会自动调用setattr()方法。getattribute()的功能与getattr()类似，用于获取属性的值。但是getattribute()能提供更好的控制，代码更健壮。注意，python中并不存在setattribute()方法。代码例子：

class Fruit(object):
def init(self, color="red", price=0):
self.color = color
self.price = price

def __getattribute__(self, item):              # <span style="font-family:宋体;font-size:12px;">获取属性的方法</span>  
    return object.__getattribute__(self, item)  

def __setattr__(self, key, value):  
    self.__dict__[key] = value  
if name == "main":
fruit = Fruit("blue", 10)
print fruit.dict.get("Fruitcolor") # 获取color属性
fruit.dict["_Fruitprice"] = 5
print fruit._dict.get("_Fruitprice") # 获取price属性
　　Python不允许实例化的类访问私有数据，但你可以使用object._classNameattrName访问这些私有属性。

　　getitem():如果类把某个属性定义为序列，可以使用getitem()输出序列属性中的某个元素.假设水果店中销售多钟水果，可以通过getitem()方法获取水果店中的没种水果。代码例子：

class FruitShop:
def getitem(self, i): # 获取水果店的水果
return self.fruits[i]

if name == "main":
shop = FruitShop()
shop.fruits = ["apple", "banana"]
print shop[1]
for item in shop: # 输出水果店的水果
print item,
　　输出： banana
apple banana

　　str():str()用于表示对象代表的含义，返回一个字符串.实现了str()方法后，可以直接使用print语句输出对象，也可以通过函数str()触发str()的执行。这样就把对象和字符串关联起来，便于某些程序的实现，可以用这个字符串来表示某个类。代码例子：

class Fruit:
'''''Fruit类''' #为Fruit类定义了文档字符串
def str(self): # 定义对象的字符串表示
return self.doc

if name == "main":
fruit = Fruit()
print str(fruit) # 调用内置函数str()触发str()方法，输出结果为:Fruit类
print fruit #直接输出对象fruit,返回str()方法的值，输出结果为:Fruit类

　　call():在类中实现call()方法，可以在对象创建时直接返回call()的内容。使用该方法可以模拟静态方法。代码例子:

class Fruit:
class Growth: # 内部类
def call(self):
print "grow ..."

grow = Growth()      # 调用Growth()，此时将类Growth作为函数返回,即为外部类Fruit定义方法grow(),grow()将执行__call__()内的代码  
if name == 'main':
fruit = Fruit()
fruit.grow() # 输出结果：grow ...
Fruit.grow() # 输出结果：grow ...

五. 类属性、实例属性、类方法、实例方法以及静态方法

　　在了解了类基本的东西之后，下面看一下python中这几个概念的区别。

　　先来谈一下类属性和实例属性

　　在前面的例子中我们接触到的就是类属性，顾名思义，类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，这个和C++中类的静态成员变量有点类似。对于公有的类属性，在类外可以通过类对象和实例对象访问。

class people:
name = 'jack' #公有的类属性
__age = 12 #私有的类属性

p = people()

print p.name #正确
print people.name #正确
print p.age #错误，不能在类外通过实例对象访问私有的类属性
print people.age #错误，不能在类外通过类对象访问私有的类属性
　　实例属性是不需要在类中显示定义的，比如：

class people:
name = 'jack'

p = people()
p.age =12
print p.name #正确
print p.age #正确

print people.name #正确
print people.age #错误
　　在类外对类对象people进行实例化之后，产生了一个实例对象p，然后p.age = 12这句给p添加了一个实例属性age，赋值为12。这个实例属性是实例对象p所特有的，注意，类对象people并不拥有它（所以不能通过类对象来访问这个age属性）。当然还可以在实例化对象的时候给age赋值。

class people:
name = 'jack'

#__init__()是内置的构造方法，在实例化对象时自动调用  
def __init__(self,age):  
    self.age = age  
p = people(12)
print p.name #正确
print p.age #正确

print people.name #正确
print people.age #错误
　　如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。

class people:
country = 'china'

print people.country
p = people()
print p.country
p.country = 'japan'
print p.country #实例属性会屏蔽掉同名的类属性
print people.country
del p.country #删除实例属性
print p.country

　　下面来看一下类方法、实例方法和静态方法的区别。

　　类方法：是类对象所拥有的方法，需要用修饰器"@classmethod"来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以"cls"作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。

class people:
country = 'china'

#类方法，用classmethod来进行修饰  
@classmethod  
def getCountry(cls):  
    return cls.country  
p = people()
print p.getCountry() #可以用过实例对象引用
print people.getCountry() #可以通过类对象引用
　　类方法还有一个用途就是可以对类属性进行修改：

class people:
country = 'china'

#类方法，用classmethod来进行修饰  
@classmethod  
def getCountry(cls):  
    return cls.country  

@classmethod  
def setCountry(cls,country):  
    cls.country = country  
p = people()
print p.getCountry() #可以用过实例对象引用
print people.getCountry() #可以通过类对象引用

p.setCountry('japan')

print p.getCountry()
print people.getCountry()

　　运行结果：

china
china
japan
japan

　　结果显示在用类方法对类属性修改之后，通过类对象和实例对象访问都发生了改变。

　　实例方法：在类中最常定义的成员方法，它至少有一个参数并且必须以实例对象作为其第一个参数，一般以名为'self'的变量作为第一个参数（当然可以以其他名称的变量作为第一个参数）。在类外实例方法只能通过实例对象去调用，不能通过其他方式去调用。

class people:
country = 'china'

#实例方法  
def getCountry(self):  
    return self.country  
p = people()
print p.getCountry() #正确，可以用过实例对象引用
print people.getCountry() #错误，不能通过类对象引用实例方法
　　静态方法：需要通过修饰器"@staticmethod"来进行修饰，静态方法不需要多定义参数。

class people:
country = 'china'

@staticmethod  
#静态方法  
def getCountry():  
    return people.country  
print people.getCountry()
　　对于类属性和实例属性，如果在类方法中引用某个属性，该属性必定是类属性，而如果在实例方法中引用某个属性（不作更改），并且存在同名的类属性，此时若实例对象有该名称的实例属性，则实例属性会屏蔽类属性，即引用的是实例属性，若实例对象没有该名称的实例属性，则引用的是类属性；如果在实例方法更改某个属性，并且存在同名的类属性，此时若实例对象有该名称的实例属性，则修改的是实例属性，若实例对象没有该名称的实例属性，则会创建一个同名称的实例属性。想要修改类属性，如果在类外，可以通过类对象修改，如果在类里面，只有在类方法中进行修改。

　　从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。

Edit By MaHua Edit By MaHua