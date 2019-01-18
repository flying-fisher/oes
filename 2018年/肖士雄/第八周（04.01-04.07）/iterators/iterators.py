'''
Created on 2018/4/3

@author: xiaoguan
'''

x = [1, 2, 3]
y = iter(x)
z = iter(x)
print(next(y))

print(next(y))

print(next(z))

print(type(x))

print(type(y))

