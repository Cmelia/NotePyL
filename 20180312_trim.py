# -*- coding: utf-8 -*-
#在不用strip的情况下去除字符串两边的空格

def trim(s):
    if s[0]==' ':
        s=s[1:]
        trim(s)
    elif s[-1]==' ':
        s=s[:-1]
        trim(s)
    else:
        print(len(s))
    #trim(s)
    #print s

trim("  Hello ")
