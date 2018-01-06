# -*- coding:utf-8 -*-

from sys import argv
import codecs

script, filename = argv

def yjiafa(a,b):
    return a+b

def print_suoyou(fh):
    print(fh.read())

def rewind(fh):
    fh.seek(0)

def print_a_line(line_count,fh):
    print(line_count, fh.readline())

fh1 = codecs.open(filename,'r',encoding='utf-8')

print("先让我们打印出文件的所有内容:\n")
print_suoyou(fh1)

print("现在让我们回到文件最前面,就像录音机倒带一样.")
rewind(fh1)

print("我们来打印第三行.")
hanghao = 1
fh1.readline()

hanghao = hanghao+1
fh1.readline()

hanghao = hanghao+1
print_a_line(hanghao,fh1)

fh1.seek(0)
hanghao = 1
print_a_line(hanghao,fh1)

fh1.close()
