from datetime import datetime, timedelta
relise = datetime(2022,11,8,12)

data = input()

new_data = datetime.strptime(data, "%d.%m.%Y %H:%M")

days_out = relise - new_data

if days_out > timedelta(days= 1):
    print(f'До выхода курса осталось: {days_out.days} дней и {days_out.seconds//3600} часов')
elif days_out < timedelta(days= 1):
    print(f'До выхода курса осталось: {days_out.seconds//3600} час и {(days_out.seconds//60)%60} минут')
elif days_out < timedelta(days= 1) and (days_out.seconds//60)%60 == 0:
    print(f'До выхода курса осталось: {days_out.seconds//3600} часа')