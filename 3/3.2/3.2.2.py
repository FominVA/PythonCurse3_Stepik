from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))