from datetime import date, timedelta
count = 5
start = date(2022, 3, 8)

g = [(start+timedelta(x)).strftime("%Y-%m-%d") for x in range(count)]
print(g)
