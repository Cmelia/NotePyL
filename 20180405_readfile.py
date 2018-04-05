# -*- coding: utf-8 -*-
import os

pwd=os.path.expanduser(r"~/readtest.txt")
with open(pwd,'r') as f:
    words=f.readlines()
    for line in words:
        print line.strip('\n')
        print line.split(' ')  # array
        print line.split()[0]




