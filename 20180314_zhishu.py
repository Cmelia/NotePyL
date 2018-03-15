def zhishu(l):
    zhi=[]
    while(True):
        zhi.append(l[0])
        t=l[0]
        def fn(n):
            return n%t != 0
        f=filter(fn,l)
    if zhi:
        print zhi

l=[2,3,4,5,6,7,8,9,10,11,12,13]
zhishu(l)
