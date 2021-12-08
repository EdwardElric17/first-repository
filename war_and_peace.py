book = [str(i) for i in input().lower().split()]
m = {}
for i in book:
    if i in m:
        m[i] += 1
    elif i not in m:
        m[i] = 0
        m[i] += 1
for key, value in m.items():
    print(key, value)
