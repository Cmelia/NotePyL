# -*- coding:utf-8 -*-
#利用闭包返回一个计数器函数，每次调用它返回递增整数

def createCounter():
    fs=[]
    def f(j):
        def counter():
            return 1+j
        return counter
    for i in range(5):
        fs.append(f(i))
    return fs

a,b,c,d,e=createCounter()
print [a(),b(),c(),d(),e()]


