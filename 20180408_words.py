#-*- coding: utf-8 -*-
import os
pwd=os.path.expanduser(r"~/readtest.txt")
file_object=open(pwd)
dict={}
for line in file_object:
    line=line.replace(","," ")
    line=line.replace("."," ")
    line=line.replace("!"," ")
    strs= line.split();
    for str in strs:
        if dict.has_key(str):
            dict[str]+=1
        else:
            dict[str]=1
result=sorted(dict.items(),key=lambda k:k[1],reverse=True)
print result
