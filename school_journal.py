m = []
u = []
s = 0
q = 0
n = 0
aver_stud = []
aver_mark = []
with open('dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        m = [str(i) for i in line.strip().split(';')]
        u.append(m)
for i in u:
    n += 1
for i in range(n):
    s = 0
    for j in range(1, 4):
        s += int(u[i][j])
    aver_stud.append(s / 3)
for j in range(1, 4):
    q = 0
    for i in range(n):
        q += int(u[i][j])
    aver_mark.append(q / n)
with open('file.txt', 'w') as ouf:
    for i in aver_stud:
        ouf.write(str(i) + '\n')
    for j in aver_mark:
        ouf.write(str(j) + ' ')

        
        

        