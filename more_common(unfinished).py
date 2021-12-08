a = {}
b = {}
s = []
k = str()
v = int()
with open("dataset_3363_3.txt", 'r') as inf:
    for line in inf:
        s += (str(i) for i in line.split())
for key in s:
    if key not in a:
        a[key] = 0
    if key in a:
        a[key] += 1
for key, value in a.items():
    if int(value) > v:
        v = int(value)
        k = key
b[k] = v
print(b)
for key, value in a.items():
    if int(value) == v:
        b[key] = value
