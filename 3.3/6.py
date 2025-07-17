from datetime import datetime
with open('diary.txt') as file:
    rows = file.read().split("\n\n")
    print(rows)