import os

path = os.path.expanduser(r"~/hello_world.txt")
f=open(path,'w+')
for i in range(100):
    f.write( str(i)+"\n" )
f.seek(0)

for i in range(10):
    path1 = os.path.expanduser(r"~/hello_world_%s.txt" % i)
    with open(path1,'w') as f1:
        for j in range(10):
            str = f.readline()
            f1.write( str )
    f.seek((i+1)*10)
    print((i+1)*10)
f.close()



