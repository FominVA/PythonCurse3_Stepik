from datetime import date, timedelta

def dates(start, count=None):
    while True:
        if count is None:
            yield start
            start += timedelta(1)
        else:
            g = [lambda x: x+timedelta(1) for x in range(count)]
            yield g


generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))