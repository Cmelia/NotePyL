# -*- coding:utf-8 -*-
# 传入一组数，返回最大值最小值

def MinMax(L):
    if L:
        Max =L[0]
        Min =L[0]
        for i in L:
            if Max<i:
                Max=i
        for j in L:
            if Min>j:
                Min=j
        print(Min,Max)

    else:
        print('(None,None)')

MinMax([1,2,3,6,8,3])
