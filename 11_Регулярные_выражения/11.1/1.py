import re

pattern = r'[sS].{4}k'

strings = [
    's.4k',
    'stepik',
    'S.{4}k',
    's4k',
    'S....k',
    's....k',
    'S4444k',
    'Stepik',
    's.{4}k',
    'S.4k'
]

for string in strings:
    if re.match(pattern, string):
        print(f'Строка "{string}" \033[92mсоответствует\033[0m рег. выражению {pattern}')
    else:
        print(f'Строка "{string}" \033[91mне соответствует\033[0m рег. выражению {pattern}')