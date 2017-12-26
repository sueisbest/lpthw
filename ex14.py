# -*- coding:utf-8 -*-

from sys import argv
script, user_name = argv
print(type(argv))
print(argv)
prompt = ">"

print("Hi %s, 我是脚本: %s."%(user_name, script))
print("我想问你几个问题.")
print("你喜欢我吗, %s ?"% user_name)
likes = input(prompt)

print("你住在哪, %s?"% user_name)
lives = input(prompt)

print("你的笔记本电脑能用几个小时, %s ?"% user_name)
battery_time = input(prompt)

print('''
嗯,对于是否喜欢我,你说%r,
你住在%r,
你的笔记本能用%r 小时
'''% (likes,lives,battery_time))
