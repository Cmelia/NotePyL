digit={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'.':'.'}

def str2float(s):
    return digit[s]

l=map(str2float,'1234.435')
le=len(l)
print le
n=l.index('.')

def fn(x,y):
    return x*10+y

shu=reduce(fn,[reduce(fn,l[:4])]+l[5:])

c=le-n-1
shu=shu*0.1**c

print shu




def str2float(s):
    digit = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, '.': '.'}
    l = list(map(lambda c: digit[c], s))
    n = l.index('.')
    l.remove('.')
    return reduce(lambda x, y: 10*x+y, l)/(10**(len(l)-n))
