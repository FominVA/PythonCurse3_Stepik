numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}

numbers = sorted(numbers)
group = sorted(group)

for i in range(len(numbers)):
    if i in group:
        del numbers[numbers.index(numbers[i])]
        numbers.insert(i)
print(numbers)