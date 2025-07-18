from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), 
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), 
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), 
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), 
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), 
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), 
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), 
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), 
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), 
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), 
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), 
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

count = 0
for t in times_of_purchases:
    if t.hour < 12:
        count += 1
    else:
        count -= 1

if count > 0:
    print('До полудня')
else:
    print("После полудня")
        
