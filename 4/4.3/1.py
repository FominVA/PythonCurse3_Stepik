
import json

with open('test.json') as file:
    data = json.load(file)                # передаем файловый объект
    for key, value in data.items():
        print(f'{key}: {value}')