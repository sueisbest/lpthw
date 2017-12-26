# -*- coding:utf-8 -*-

from  sys import argv
import codecs
from os.path import  exists

script, from_file, to_file = argv

print("从 %s 复制内容,拷贝到 %s."% (from_file,to_file))

from_file_handle = codecs.open(from_file,'r',encoding='utf-8')

from_file_data = from_file_handle.read()

print("要拷贝的文件长度是%s."% len(from_file_data))
print("接收内容的文件存在吗? %r."% exists(to_file))
input("直接按回车将继续, 按 ctrl+c 放弃.请按键-->")

to_file_handle = codecs.open(to_file,'w',encoding='utf-8')
to_file_handle.write(from_file_data)

print("写好了!")

from_file_handle.close()
to_file_handle.close()
