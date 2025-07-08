from datetime import date


def get_date_range(date1,date2):
    result =[]
    for i in range(date.toordinal(date1),date.toordinal(date2)+1):
        a = date.fromordinal(i)
        result.append(a)
    return result


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='')