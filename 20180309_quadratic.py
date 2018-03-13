# -*- coding: utf-8 -*-
#定义一个函数quadratic(a,b,c)，接受三个参数，返回一元二次方程的根。
#ax^2+bx+c=0

import math

def quadratic(a,b,c):
    x1=((-b+math.sqrt(b**2-4*a*c))/(2*a))
    x2=((-b-math.sqrt(b**2-4*a*c))/(2*a))
    return x1,x2

print(quadratic(2,-1,-3))
