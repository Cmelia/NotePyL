# -*- coding:utf-8 -*-
import re
# 形如AB:AB AA:BB AB:BA的时间，称为Lucky time,
# 要求，第一行输入一个数n,第二行输入n个字符串形如“HH:MM”，字符串间以空格分割
# 输出一个整数，表示一共有多少个幸福时刻

#接受输入的两行数
a=raw_input('请输入第一行')
print a
b=raw_input('请输入第二行')
#b='11:22 13:43 13:13 44:35 56:65'

print b
#如何限制第一行的1<=n<=50,第二行的字符串的个数正好等于n

#判断b中的字符串是不是幸福时刻
#先把b中的字符串split成单词
bs=b.split()

def check(word):
    #pattern=re.compile(r'\b([0-9])\1\b:\b([0-9])\1\b')
    pattern=re.compile(r'(\d)\1:([0-9])\2|(\d)(\d):\2\12|(\d)(\d):\1\2')
    if pattern.search(word):
        return word

for w in bs:
    print check(w)




