# -*- coding:utf-8 -*-

maruixin = {}
maruixin['age'] = 11
maruixin['hight'] = 155
maruixin['money'] = 1000
maruixin['friends'] = 'xxx,xxx,xxx,xxx'
print('马瑞欣:',maruixin)

ydict = {}
ydict['mrx'] = {'age':12,'money':1000,'friends':['yishu','qsa']}
ydict['mrx']['friends'].append('ljy')
print(ydict)

ydict['yishu'] = {'age':11,'money':140,'friends':['mrx','czx']}
ydict['yishu']['friends'].append('qje')
print(ydict)
ydict['yishu']['money'] += 1000

print(ydict)

if ydict['mrx']['money'] > ydict['yishu']['money']:
    print('mrx很坏.')
else:
    print('yishu很好.')
