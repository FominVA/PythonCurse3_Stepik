import sys

data = list(map(int, sys.stdin))
n = len(data)
def func(n):
    if n >= 0:
        print(data[n])
        func(n-1)
func(n)