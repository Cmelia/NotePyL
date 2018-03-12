# -*- coding: utf-8 -*-

#可以接受一个或多个数并计算乘积

def product(*args):
    s=1
    for i in args:
        s=s*i
    print s

product(1,3,4,5)
