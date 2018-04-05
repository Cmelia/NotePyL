for n in range(0,100,10):
    with open('file', 'r') as reader, open(str(n // 10)+".txt", 'w') as writer:
        for index, line in enumerate(reader):
            if index >=n and index < n+10:
                writer.write(line)



with open('txt') as f:
    for line in f.readlines():
        print line.split('\t')[0]


