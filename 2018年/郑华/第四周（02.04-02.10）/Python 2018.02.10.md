# Python 2018.02.10

标签（空格分隔）： 基本概念要点

---

 


 - 字符串单双引号通用，利用三引号，可以指示一个多行的字符串；


----------


## 例如: ##
'''This is a multi-line string. 
This is the first line.
This is the second line.
"What's your name?," I asked.He said "Bond, James Bond."
'''
这里单双引号都是无需加转义符"\"


----------



 - 使用变量时只需要给它们赋一个值，不需要声明或定义数据类型；
 - 建议在每个物理行只写一句逻辑行，少用分号；
 - 统一缩进，每个缩进层次使用单个制表符或两个或四个空格；
 - 控制语句if/elif/else；while/else；for...in/else；


----------
## 举例if： ##
number = 26
guess = int(raw_input('Enter an integer : '))

if guess == number:
    print 'Congratulations, you guessed it.' 
    print "(but you do not win any prizes!)" 
elif guess < number:
    print 'No, it is a little higher than that' 
else:
    print 'No, it is a little lower than that' 
print 'Done'

$ python if.py

Enter an integer : 50
No, it is a little lower than that
Done

$ python if.py

Enter an integer : 25
No, it is a little higher than that
Done

$ python if.py

Enter an integer : 26
Congratulations, you guessed it.
(but you do not win any prizes!)
Done 

## 举例while ##
number = 26
running = True
while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.' 
        running = False 
    elif guess < number:
        print 'No, it is a little higher than that' 
    else:
        print 'No, it is a little lower than that' 
else:
    print 'The while loop is over.' 
print 'Done' 

$ python while.py
Enter an integer : 50
No, it is a little lower than that.
Enter an integer : 22
No, it is a little higher than that.
Enter an integer : 23
Congratulations, you guessed it.
The while loop is over.
Done 

## 举例for in ##
for i in range(1, 5):
    print i
else:
    print 'The for loop is over' 

$ python for.py
1
2
3
4
The for loop is over


----------


- break；continue；return；
- 函数：def/global





