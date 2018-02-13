# -*- coding:utf-8 -*-

yas = [100, -1, 50, 22, 100, 0, 88]

for a in range(0, len(yas) - 1):
    for i in range(0, len(yas) - a - 1):
        if yas[i] > yas[i + 1]:
            yas[i], yas[i + 1] = yas[i + 1], yas[i]
        else:
            pass

print(yas)

for a in range(0, len(yas) - 1):
    for i in range(0, len(yas) - a - 1):
        if yas[i] < yas[i + 1]:
            yas[i], yas[i + 1] = yas[i + 1], yas[i]
        else:
            pass

print(yas)
