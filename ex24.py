# -*- coding:utf-8 -*-

print("\"我能打出双引号\"")
mozi = "\t志不强者智不达,言不信者信不果. \n\t\t据财不能分人者,不足与友:" \
    "\n\t\t\t守道不笃,偏物不博,辩是非不察者,\n\t\t\t\t不足与游."

print('-'*49)
print(mozi)
print('-'*23+'墨子'+'-'*23)

六 = 11-2+3-6
print("这个数应该是六: %s" %六)

print("输入一个以秒为单位的时长,函数可以帮你快速将这个时长转换为周/天/小时/分钟.")
def quickMath(starSecs):
    weeks = starSecs/(7*24*60*60)
    days = weeks*7
    hours = days*24
    mins = hours*60
    weeks = round(weeks,2)
    days = round(days,2)
    hours = round(hours,2)
    mins = round(mins,2)
    return weeks,days,hours,mins

mySecs = 31449666
myWeeks,myDays,myHours,myMins = quickMath(mySecs)

print("如果是%s秒, 则它相当于:" %mySecs)
print("%s周;或\n%s天;或\n%s小时;或\n%s分钟" %(myWeeks,myDays,myHours,myMins))

print("少年们,时不我待,用好自己的时间.")
