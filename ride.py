"""
ID:sueyi201
LANG:PYTHON3
TASK:ride
"""

ydict = {}

for i in range(65,91):
    ydict[chr(i)] = i-64
'''
yshu = ord('M')
print(yshu)

print(ydict['M'])

astring = 'BCD'
alist = list(astring)

b = ord(alist[0])
c = ord(alist[1])
d = ord(alist[2])
print(b * c * d)

product = 1
aString = 'BCDEA'
aList = list(aString)

for each_chr in aList:
    product = product * ydict[each_chr]

print(product)
'''
fin = open('ride.in','r')
fout = open('ride.out','w')
yufo = fin.readline().strip()
ygroup = fin.readline().strip()

listyufo = list(yufo)
listygroup = list(ygroup)

ufoproduct = 1
groupproduct = 1
for each_element in listyufo:
    ufoproduct = ufoproduct * ydict[each_element]

for each_element in listygroup:
    groupproduct = groupproduct * ydict[each_element]

if ufoproduct % 47 == groupproduct % 47:
    fout.write('GO'+'\n')
else:
    fout.write('STAY'+'\n')
