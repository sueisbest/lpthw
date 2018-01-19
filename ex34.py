# -*- coding:utf-8 -*-

animals = ['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
'''
j = 0
x = 1
for i in range(0,12):
    print("第%s只动物在位置%s,是一只%s.在位置%r的是第%r只动物,是1只%r" % (x, j, animals[j], j, x, animals[j]))
    j = j+1
    x = x+1
'''
for i in range(0,12):
    print("第%s只动物在位置%s,是一只%s.在位置%r的是第%r只动物,是1只%r" % (i+1, i, animals[i], i, i+1, animals[i]))
