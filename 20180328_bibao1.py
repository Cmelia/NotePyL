def count():
    fs=[]
    for i in range(4):
        def f():
            return i*i
        fs.appened(f())
    return fs
