# -*- coding:utf-8 -*-

def dogs_and_cats(dog_count,cat_count):
    print("你有%s只狗!" % dog_count)
    print("你有%s只猫!" % cat_count)
    print("多了管不过来.")
    print("给它们吃点东西.\n")

print("我们可以直接给函数提供数字.")
dogs_and_cats('abc',31)

print("函数的参数也可以是我们的变量.")
num_of_dogs = 22
num_of_cats = 23

print("还可以在参数中使用加减法.")
dogs_and_cats(1+12,3+7)

print("加减法还可以和变量结合起来.")
dogs_and_cats(num_of_dogs+5,num_of_cats+15)
