from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(days=7, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))