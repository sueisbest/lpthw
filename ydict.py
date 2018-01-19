# -*- coding:utf-8 -*-
'''
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
'''
fin = open('ydict.in','r')
fout = open('ydict.out','w')
ydict = {}
names=[]

for j in range(2):

    name=fin.readline().strip()
    line_splitted=fin.readline().strip().split()
    money,no_of_fri=int(line_splitted[0]),int(line_splitted[1])
    friends=[]
    for i in range(no_of_fri):
        friends.append(fin.readline().strip())
    ydict[name]={'money':money,'friends':friends}
    names.append(name)


'''
ydict[fin.readline().strip()] = {'money,friends':fin.readline().strip(),'friends':[fin.readline().strip(),fin.readline().strip(),fin.readline().strip()]}
ydict[fin.readline().strip()] = {'money,friends':fin.readline().strip(),'friends':[fin.readline().strip(),fin.readline().strip(),fin.readline().strip(),fin.readline().strip()]}
print(ydict)
fout.write('马瑞欣 1000')
'''

for each_name in names:
    fout.write(each_name+' '+str(ydict[each_name]['money'])+'\n')

fin.close()
fout.close()

print("我成功了!")
