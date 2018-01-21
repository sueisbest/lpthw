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
for i in range(num_of_names):
    names.append(fin.readline().strip())

for each_name in names:
    ydict[each_name] = {'rs':0, 'rem':0, 'give':0, 'money':0, 'yget':0, 'num_of_friends':0, 'friends':[]}

for i in range(num_of_names):
    name = fin.readline().strip()
    ysplit = fin.readline().strip().split()
    ydict[name]['money'], ydict[name]['num_of_friends'] = int(ysplit[0]),int(ysplit[1])
    if ydict[name]['num_of_friends'] != 0:
        ydict[name]['give'] = ydict[name]['money'] // ydict[name]['num_of_friends']
        for i in range(ydict[name]['num_of_friends']):
            ydict[name]['friends'].append(fin.readline().strip())
    else:
        continue
    if ydict[name]['money'] != 0:
        ydict[name]['rem'] = ydict[name]['money'] % ydict[name]['num_of_friends']
    else:
        ydict[name]['rem'] = 0
    for each_friend in ydict[name]['friends']:
        ydict[each_friend]['yget'] += ydict[name]['give']

for each_name in names:
    ydict[each_name]['rs'] = ydict[each_name]['rem'] + ydict[each_name]['yget'] - ydict[each_name]['money']
    a = each_name + ' ' + str(ydict[each_name]['rs']) + '\n'
    fout.write(a)

fin.close()
fout.close()
