# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

print("警告,系统将擦除文件 %r ." %filename)
print("如果你还没有准备好, 请按停止键 ctrl+c.")
print("如果没问题, 请按回车键.")

input("直接按回车键将继续.")

print("正在打开文件...")
f = open(filename,'w')

print("擦除文件中...")
f.truncate()

print("现在,我需要你输入三行文本.")
line1 = input("第一行: >>>")
line2 = input("第二行: >>>")
line3 = input("第三行: >>>")

print("我要把这些写入文件中.")

f.write(line1)
f.write("\n")
f.write(line2)
f.write("\n")
f.write(line3)
f.write("\n")

print("文件写好了. 现在,我们关闭文件.")
f.close()
print("文件成功关闭.")
