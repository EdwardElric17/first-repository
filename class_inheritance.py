di = {'object':[]}
def dict_complation(a):
    lst1 = []
    lst1.extend(a.split())
    return lst1
def dict_inheritance(lst):
    if len(lst) == 1:
        di['object'] += lst[0]
    else:
        for i in range(len(lst)):
            if i > 1:
                if lst[i] not in di.keys():
                    di[lst[i]] = []
                di[lst[i]] += lst[0]
    return di
def check_classes(di):
    lst2 = []
    lst2 += (str(i) for i in input().split())
    if lst2[1] in di[lst2[0]]:
        print('Yes')
    else:
        search_in_di(lst2[0], lst2[1], di)
def search_in_di(a, b, c):
    for i in c[a]:
        if b in c[i]:
            return 'Yes'
        else:
            search_in_di(i, b, c)
    print('No')
for i in range(int(input())):
    dict_inheritance(dict_complation(str(input())))
for i in range(int(input())):
    check_classes(di)