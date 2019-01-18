# Python函数

标签（空格分隔）： 2018.3.10

---
## 匿名函数 lambda ##
可以省略不常用的函数定义：
```
def add(x,y)
    return x+y
```
等价于`add = lambda x,y :x+y    `
## filter 与 map ##
```
>>>list(filter(lambda x:(x+1) % 2 ,range(10)))
>>>[0, 2, 4, 6, 8]
```
```
>>>list(map(lambda x:x*x ,range(5)))
>>>[0, 1, 4, 9, 16]
```
## 迭代与递归 ##
```
#  -*- coding: utf-8 -*-
def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n-1)
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
number = int(input ("请输入正整数n："))
result1 = recursion(number)
result2 = factorial(number)
print "迭代法计算%d的阶乘为%d" %(number,result2)
print "递归法计算%d的阶乘为%d" %(number,result1)

请输入正整数n：5
迭代法计算5的阶乘为120
递归法计算5的阶乘为120

```
**汉诺塔：**
```
# -*- coding: utf-8 -*-
def hanoi(n,x,y,z):
    if n == 1:
        print "从%s移动到%s" %(x,z)
    else:
        hanoi(n-1,x,z,y)
        print  "从%s移动到%s" %(x,z)
        hanoi(n-1,y,x,z)
n = int (input('请输入汉诺塔层数： '))
hanoi(n,'X','Y','Z')

请输入汉诺塔层数： 3
从X移动到Z
从X移动到Y
从Z移动到Y
从X移动到Z
从Y移动到X
从Y移动到Z
从X移动到Z
```

   