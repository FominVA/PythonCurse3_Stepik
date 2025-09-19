from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
m = max(data.values())
print(m)
# print(list(filter(lambda x: max(x.value()), data.most_common())))
# data.__dict__['min_value'] = lambda: min(data.values())
# data.__dict__['max_value'] = lambda: max(data.values())