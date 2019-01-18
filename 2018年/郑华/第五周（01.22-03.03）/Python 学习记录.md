# Python 学习记录

标签（空格分隔）： 2018.3.3

---

 **1. 复习回顾**
 


----------

猜数小游戏：
整理使用了if、While、random.randint以及条件表达式（三元操作符）和基本操作
```
import random
secret = random.randint(1,50)
i = 1
temp = input("You have five chances to guess between[1,50]: ")
guess = int(temp)
if guess == secret:
        print "Right!\nCongratulations!" #Python3 需要加括号
else:
    while (guess != secret) and (i < 6):
        print "Larger" if guess > secret else "Smaller"
        i += 1
        temp = input("guess again: ")
        guess = int(temp)
        if guess == secret:
            print "Right!\nGreat!"
            break
    if i >= 6:
        print "Game over!"
```
```
You have five chances to guess between[1,50]: 3
Smaller
guess again: 34
Larger
guess again: 15
Smaller
guess again: 25
Smaller
guess again: 29
Smaller
guess again: 32
Game over!
```


----------


 **2. 列表**
以数组name=[1,2,3,4]为例：
（1）添加：
```
name.append(5)添加单个元素;
extend([5,6])添加列表（相当于添加末尾元素）;
insert(位置，元素)；
```
（2）互换：
``` 
name[1], name[2] = name[2], name[1]
```
（3）删除：
``` 
name.remove("blabla")```
``` 
```
name.del[1] 
del name   #del是语句无括号
```
```
name.pop() #弹出并删除最后一个元素
name.pop(1) #弹出并删除最后对应元素
```
（4）分片拷贝：
```
name[0:2] #输出0、1 两个位置元素，不包括末位置
name[:3] #输出0、1、2三个位置的元素
name[1:] #输出第二个位置起的元素
name[0:10:2] #输出间隔为2的0-9共5个位置的元素
name[::-1] #反序提取，与reverse不同
```
**注意：**
name2=name1[:]为分片拷贝，不受name1变化影响

（5）计算次数：name.count(XXX)
（6）返回位置：name.index(XXX) #第一个
```
#返回第二个位置
start = name.index(XXX)+1
stop = len(name)
name.index(XXX, start, stop)

```
（7）翻转：name.reverse（）
（8）排序：name.sort（func, key, reverse）,默认reverse=False为从小到大
（9）列表其它操作：
+拼接，*复制多次后拼接

----------
 **3. 元组：**不可删改的列表！
```
tuple = ()
tuple = (1,)
3 * (3) == 9
3 * (3,) == (3, 3, 3)
del tuple #删除元组
```
----------


 **4. 其它补充：**
assert XXX == (if XXX == False break)

