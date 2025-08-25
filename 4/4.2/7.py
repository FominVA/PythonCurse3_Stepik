import csv

with open('wifi.csv', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    districts = {}
    
    for row in reader:
        district = row['district']
        count = int(row['number_of_access_points'])
        districts[district] = districts.get(district, 0) + count
    sorted_districts = sorted(districts.items(), key=lambda item: (-item[1], item[0]))

    for row in sorted_districts:
        print(f'{row[0]}: {row[1]}')
    # for key, value in d.items():
    #     s = sum([int(i) for i in value])
    #     d1.setdefault(key, []).append(s)
    # sorted_d1 = sorted(d1.items(), key=lambda item: (item[1], item[0]), reverse=True)
  
    # for key, value in sorted_d1:
    #     v = value[0]
    #     print(f'{key}: {v}')
    
            
