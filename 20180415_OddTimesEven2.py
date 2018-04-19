def is_odd(num):
    if num%2==1:
        return True
    return False

def division(n):
    for i in range(n):
        quotient=n/(i+1)
        if is_odd(i):
            if not is_odd(quotient):
                return i+1,quotient
                break
        if not is_odd(i):
            if is_odd(quotient):
                return i+1,quotient
                break


print division(5)



