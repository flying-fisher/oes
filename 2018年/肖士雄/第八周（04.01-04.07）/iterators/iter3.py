'''
Created on 2018/4/3

@author: xiaoguan
'''
from itertools import islice,cycle
colors = cycle(['red', 'white', 'blue'])  # infinite
limited = islice(colors, 0, 4)            # finite
for x in limited:                         # so safe to use for-loop on
    print(x)


