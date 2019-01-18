'''
Created on 2018/4/3

@author: xiaoguan
'''
from itertools import islice

class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self 
    
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()
print(list(islice(f, 0, 10)))


