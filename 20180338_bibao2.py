def createCounter():
    fs=[]
    for i in range(1,4):
        def counter():
            return i;
        fs.append(counter)
    return fs

f1,f2,f3=createCounter()
print f1()
print f2()
print f3()

def createCounter():
    fs=[]
    for i in range(1,4):
        def counter():
            return i;
        fs.append(counter())
    return fs

f1,f2,f3=createCounter()
print f1
print f2
print f3



def createCounter1():
    def counter1(i):
        def g():
            return i;
        return g;
    fs1=[]
    for g in range(1,4):
        fs1.append(counter1(g))
    return fs1

f11,f21,f31=createCounter1()
print f11()
print f21()
print f31()
