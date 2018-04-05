# -*- coding:utf-8 -*-

digit={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    return digit[s]

def fn(x,y):
    return x*10+y

print(map(str2int,'33454'))



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break




def multipliers():
    return [lambda x: i * x for i in range(4)]

print([m(2) for m in multipliers()])

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print Month.Jan
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

season=['spring','summer','fall','winter']
print list(enumerate(season))

