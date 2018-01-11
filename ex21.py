# -*- coding:utf-8 -*-

def add(a,b):
    print("加法:%d + %d" % (a,b))
    return a+b

def subtract(a,b):
    print("减法:%d - %d" % (a,b))
    return a-b

def multiply(a,b):
    print("乘法:%d * %d" % (a,b))
    return a*b

def divide(a,b):
    print("除法:%d / %d" % (a,b))
    return a/b

print("下面我们来用函数做点数学题.")
age = add(9,3)
height = subtract(160,4)
weight = multiply(45,2)
iq = divide(100,2)
print("年龄:%d, 身高:%d, 体重:%d, IQ:%d" % (age, height, weight, iq))
print("再来一道附加题.")
what = add(age, subtract(height, multiply(weight,divide(iq,2))))
print("结果得到:",what,"你能笔算一遍吗? 比较一下你算的顺序和计算机算的顺序.")
