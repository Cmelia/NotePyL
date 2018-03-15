from collections import Iterable


dao=0
def check(n):
    l=[]
    #global l
    global dao
    while(n/10!=0):
        num=n%10
        n=(n-num)/10
        l.append(num)
    num=n%10
    n=(n-num)/10
    l.append(num)
    def fn(x,y):
        return x*10+y
    dao=reduce(fn,l)
    return dao

def huishu(nu):
    #print nu,check(nu)
    if nu==check(nu):
        return nu

print(filter(huishu,range(1,1000)))

