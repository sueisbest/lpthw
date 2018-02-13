# -*- coding:utf-8 -*-

def gold_room():
    print("这个房间堆满了金子。你打算拿多少？")

    next = input('> ')
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead("朋友，你得输入一个小小的（非常小的）数字")

    if how_much < 50:
        print("你一点也不贪婪，你赢了！")
        exit(0)
    else:
        dead("你这个贪婪的混蛋！")

def bear_room():
    print("这里有一只熊。")
    print("这只熊有一大堆蜂蜜。")
    print("在这只胖熊的身后有一扇门。")
    print("你要怎样才能让这只熊滚蛋？")
