# 条件和循环语句

## 1.条件语句  
### 1.1 条件执行和if语句
if语句可实现条件执行，即如果条件（在if和冒号之间的表达式）判定为真，那么后面的语句块就会被执行。如果条件为假，语句块就不会被执行。

name=input(‘what is your name’)  if name.endswith(‘Gumby’):  print ‘Hello’

### 1.2 else子句

在上面例子中，如果用户输入以Gumby作为结尾的名字，那么name.endswith方法就会返回真，使得if进入语句块，打印出问候语。也可用else子句增加一种选择。

name=input(‘what is your name’)  if name.endswith(‘Gumby’):  print ‘Hello’
else:  print ‘Stranger’

如果条件被判定为假，则第1个语句块没有被执行，那么就会转入第2个语句块。

### 1.3 elif子句

如果需要检查多个条件，就可以使用elif，它是else if的简写，也是if和else子句的联合使用，也就是具有条件的else子句。

num=input(‘Enter a number:’)  if num>0:  print ‘positive’ 
elif num<0:  print ‘negative’  else:  print ‘zero’

### 1.4 嵌套代码块

在if语句里面可以嵌套使用if语句。

name=input(‘what is your name’) 
if  name.endswith(‘Gumby’):
if  name.startswith(‘Mr.’):
print ‘Mr.Gumby’
elif  name.startswith(‘Mrs.’):
print ‘Mrs.Gumby’
else:
print ‘Gumby’
else:
print ‘Stranger’

## 2.循环语句   

### 2.1 while循环

为保证程序的重复执行，可使用循环语句实现。

name=’’
while not name:
name=input(‘Please enter your name:’)
print ‘Hello, %s’ % name

运行这个程序，然后在程序要求输入名字时按下回车键。程序会再次要求输入名字，因为name还是空字符串，其求值结果为false。

### 2.2 for循环

while语句一般情况下够用，针对序列和其他可迭代对象，可使用for循环，让集合中的每个元素都执行代码块。

words=[‘this’,‘is’,’an’,’ex’,’parrot’]
for word in words:
print word

### 2.3 跳出循环

（1）break：使用break语句结束循环；

（2）continue：跳过剩余的循环体，让当前的迭代结束，“跳”到下一轮循环的开始。