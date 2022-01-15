di = {}
def dict_complation(a):
    lst1 = []
    lst1.extend(a.split())
    return lst1
def dict_inheritance(lst):
    clss2 = []
    clss1 = str()
    for i in range(len(lst)):
        if i == 0:
            clss1 = lst[0]
        if i > 1:
            clss2.append(lst[i])
    di[clss1] = clss2
    return di
def check_classes(di):
    lst2 = []
    lst2 += (str(i) for i in input().split())
    if lst2[0] in di[lst2[1]]:
        print('Yes')
    else:
        print('No')
for i in range(int(input())):
    dict_inheritance(dict_complation(str(input())))
for i in range(int(input())):
    check_classes(di)