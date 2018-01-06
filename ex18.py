# -*- coding:utf-8 -*-

def print_two(*args):
    print(args)
    arg1, arg8, *sret = args
    #arg1, arg8 = args

    print("arg1 : %r, arg8 : %r" % (arg1, arg8))
    print(sret)

def print_two_again(arg0,arg1):
    print("arg1:%r, arg0:%r" % (arg1,arg0))

def print_none():
    pass

#print_two('abc','efg',1,2,3,4,5)
#print_two_again('axf','asd')
print_none()