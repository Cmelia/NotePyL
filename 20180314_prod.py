def prod(x,y):
    return x*y

print reduce(prod,[3,5,7,9])


print sorted([22,0,-44,-5])
print sorted([22,0,-44,-5],key=abs)
