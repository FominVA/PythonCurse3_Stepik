from sys import stdin
from collections import Counter

data = list(map(str.strip, stdin))

name = [i.split(' ') for i in data]

print(name.most_common())