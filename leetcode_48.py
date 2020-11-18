import datetime
day,month,year = 31, 8, 2019

a=(datetime.datetime(year,month,day)).strftime(("%A"))
print(a)