"""
ID:sueyi201
LANG:PYTHON3
TASK:gift1
"""

fin = open('gift1.in','r')
fout = open('gift1.out','w')
ydict = {}
names=[]
num_of_names = int(fin.readline().strip())
#读gift1的第1行,有5个人.
for i in range(num_of_names):
    names.append(fin.readline().strip())
#重复运行5次,读出每个人的名字,放进names列表.

for each_name in names:
    ydict[each_name] = {'rs':0, 'rem':0, 'give':0, 'money':0, 'yget':0, 'num_of_friends':0, 'friends':[]}
#用names中的项做字典的项的键(不是 值).

for i in range(num_of_names):
    name = fin.readline().strip()
    #读出第一个人名.
    ysplit = fin.readline().strip().split()
    #读钱数和朋友数,按空格将两个字符串分开.
    ydict[name]['money'], ydict[name]['num_of_friends'] = int(ysplit[0]),int(ysplit[1])
    #把两个字符串转换成数,分别赋值给ydict[name]['money']和ydict[name]['num_of_friends'].
    #同时也修改了字典元素 ydict[name]的值; 字典的元素由于 {键:值} 对组成
    if ydict[name]['num_of_friends'] != 0:
        ydict[name]['give'] = ydict[name]['money'] // ydict[name]['num_of_friends']
        for i in range(ydict[name]['num_of_friends']):
            ydict[name]['friends'].append(fin.readline().strip())
    #如果朋友数不是0,算出他(她)要给每个朋友的钱,按照朋友的数量读出朋友,放进friends列表.
    else:
        continue
    #反之忽视后面的语句,回到循环的开头. 将继续读取一个名字,然后读取钱数和朋友数

    if ydict[name]['money'] != 0:
        ydict[name]['rem'] = ydict[name]['money'] % ydict[name]['num_of_friends']
    #如果钱数不是0,算出可能剩下的钱.
    else:
        ydict[name]['rem'] = 0
    #反之跳过.因为如果给出的钱数是0,剩下的钱肯定是0.

    for each_friend in ydict[name]['friends']:
        ydict[each_friend]['yget'] += ydict[name]['give']
    #从朋友列表中访问并修改朋友得到的钱数.

#跳出循环.
for each_name in names:
    ydict[each_name]['rs'] = ydict[each_name]['rem'] + ydict[each_name]['yget'] - ydict[each_name]['money']
    #算出每个人最后的钱.
    a = each_name + ' ' + str(ydict[each_name]['rs']) + '\n'
    ###空格是字符串,要加''.
    fout.write(a)
    ###write()只接受一个参数.

fin.close()
fout.close()
###程序结束时关闭文件.
