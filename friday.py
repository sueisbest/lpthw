# -*- coding:utf-8 -*-

"""
* black_days (i):
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
0 = Sunday

* black_days[]:
1 = Jan
2 = Feb
3 = Mar
...
"""
year = 0

month = {}
if 1900 % 400 == 0:
    month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    year = 366
else:
    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    year = 365

fblack_days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
fblack_days[1] = 13 % 7

month_days = 31
for i in range(2, 13):
    fblack_days[i] = (month_days + 13) % 7
    month_days += month[i]

month_days = 0
sblack_days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

if 1901 % 4 == 0:
    month = {1: 31, 2: 60, 3: 91, 4: 121, 5: 152, 6: 182, 7: 213, 8: 244, 9: 274, 10: 305, 11: 335, 12: 366}
    year = 366
else:
    month = {1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
    year = 365

sblack_days[1] = (year + 13) % 7
for i in range(2, 13):
    sblack_days[i] = (year + month[i - 1] + 13) % 7

print(sblack_days)

tblack_days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

if 1902 % 4 == 0:
    month = {1: 31, 2: 60, 3: 91, 4: 121, 5: 152, 6: 182, 7: 213, 8: 244, 9: 274, 10: 305, 11: 335, 12: 366}
    year = 365 + 366
else:
    month = {1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
    year = 365 + 365

tblack_days[1] = (year + 13) % 7
for i in range(2, 13):
    tblack_days[i] = (year + month[i - 1] + 13) % 7

print(tblack_days)
