digit={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'.':'.'}

def str2float(s):
    return digit[s]

l=map(str2float,'1234.435')

n=l.index('.')

def fn1(x,y):
    return x*10+y


def fn2(x,y):


    return x+y*0.1



print reduce(fn2,[reduce(fn1,l[:4])]+l[5:])
#print [reduce(fn1,l[:4])]+l[5:6]
