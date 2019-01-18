'''
Created on 2018/4/3

@author: xiaoguan
'''

from itertools import islice
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

f = fib()
print(list(islice(f, 0, 10)))



