from datetime import date

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
flag = date1 < date2
for j in range(date.toordinal(date2), date.toordinal(date1)+1):
    a = date.fromordinal(j)
    
    a = a.weekday()
    print(a)  
