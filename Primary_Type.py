import csv 

primary_types = list()
free_set = set()
max_entr = ''
with open('Crimes.csv') as ouf:
    reader = csv.reader(ouf)
    for line in reader:
        primary_types.append(line[5])
    for i in primary_types:
        free_set.add(i)
    max_count = 0
    for i in free_set:
        count = 0
        for j in primary_types:
            if j == i:
                count += 1
        if count > max_count:
            max_count = count
            max_entr = i
print(max_entr)