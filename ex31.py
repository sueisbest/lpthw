# -*- coding:utf-8 -*-

print("你进入了一间黑暗的屋子.屋子有两个门.你会穿过1号门,还是2号门?")
prompt = '->'
door = input(prompt)
if door == '1':
    print("进门后你看到了一只巨熊在吃奶油蛋糕.你会怎么做?\n1.你拿走蛋糕.\n2.你冲着熊尖叫.\n3.你对着熊抛媚眼.")
    bear = input(prompt)
    if bear == '1':
        print("巨熊咬掉了你的脸.真背!")
    elif bear == '2':
        print("巨熊咬掉了你的腿.真背!")
    elif bear == '3':
        print("巨熊被你吸引了.好样的!")
    else:
        print("你什么都没干,把巨熊惹怒了.真倒霉!")
elif door == '2':
    print("你看到了邪神的双眼,里面是无尽的黑暗.")
    print("你可以:\n1.吃个蓝莓.")
    print("2.穿双红袜子.")
    print("3.唱'当当当'")
    print("4.召唤Alpha.")
    insanity = input(prompt)
    if insanity == '1' or insanity == '2':
        print("你得救了.吃蓝莓或穿红袜子让你强大无比!")
    elif insanity == '4':
        print("伟大而又神秘的Alpha拯救了邪神腐化的心灵!")
    else:
        print("邪神的目光腐化了你的双眼.真倒霉!")
else:
    print("你四处摸索,撞在了墙上,真不走运!")
