s = []
m = []
l = 0
d = {}
with open('dataset_3380_5 (1).txt', 'r') as inf:
    for line in inf:
        s.append([str(i) for i in line.split()])
for i in range(len(s)):
    for j in range(3):
        if j == 0:
            if s[i][j] not in d:
                d[s[i][j]] = []
        if j == 2:
            d[s[i][0]].append(s[i][j])
for i in range(1, 12):
    l = 0
    if str(i) in d:
        for j in range(len(d[str(i)])):
            l += int(d[str(i)][j])
        m.append(l/len(d[str(i)]))
    if str(i) not in d:
        m.append(['-'])
k = 1
with open('text.txt', 'w') as ouf:
    for i in m:
        ouf.write(str(k) + ' ' + str(i) + '\n')
        k += 1