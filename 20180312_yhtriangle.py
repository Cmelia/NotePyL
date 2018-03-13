def yhtriangle(n):
    a=[1]
    b=[1,1]

    if n==1:
        print a
    elif n==2:
        print a
        print b
    else:
        print a
        print b
    counter =3
    while(counter<=n):

        a=b


        b=range(counter)
        b[0]=1
        b[counter-1]=1
        for i in range(1,counter-1):
            b[i]=a[i]+a[i-1]
        counter+=1
        yield b

t=yhtriangle(3)
for j in t:
    print j
