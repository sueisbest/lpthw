# -*- coding:utf-8 -*-

from sys import argv
import codecs

script, filename = argv
#f = codecs.open(filename,'r',encoding='utf-8')
f = codecs.open(filename,'r',encoding='GBK')

print("这是你的文件 %r --"%filename)
print(f.read())

print("再次输入文件名.")
file_again = input("<>")

f = codecs.open(file_again,'r',encoding='utf-8')
print(f.read())

f.close()