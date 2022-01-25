di = {'object':[]}
lst1 = []
lst2 = []
g = bool()
def check_exepts(exept1, exept2):
    global g
    if exept1 in di[exept2]:
        g = True
        print(exept1)
    else:
        for k in range(len(di[exept2])):
            check_exepts(exept1, di[exept2][k])
for i in range(int(input())):
    lst1 = []
    for clas in input().split():
        lst1.append(clas)
    if len(lst1) == 1:
        di['object'].append(lst1[0])
    else:
        for j in range(len(lst1)):
            if j > 1:
                if lst1[j] not in di:
                    di[lst1[j]] = []
                di[lst1[j]].append(lst1[0])
    if lst1[0] not in di:
        di[lst1[0]] = []
lst1 = []
for i in range(int(input())):
    for clas in input().split():
        if clas not in lst1:
            lst1.append(clas)
for exept1 in lst1:
    if (len(lst2)) == 0 or (exept1 in di['object']):
            lst2.append(exept1)
    else:
        for exept2 in lst2:
            check_exepts(exept1, exept2)
        if g != True:
            lst2.append(exept1)