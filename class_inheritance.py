di = {'object':[]}
g = str()
def dict_complation(a):
    lst1 = []
    lst1.extend(a.split())
    return lst1
def dict_inheritance(lst):
    if lst[0] not in di:
        di[lst[0]] = []
    if len(lst) == 1:
        di['object'].append(lst[0])
    else:
        for i in range(len(lst)):
            if i > 1:
                if lst[i] not in di.keys():
                    di[lst[i]] = []
                di[lst[i]].append(lst[0])
    return di
def check_classes(di):
    global g
    lst2 = []
    lst2 += (str(i) for i in input().split())
    if lst2[0] == lst2[1]:
        print('Yes')
    elif lst2[1] in di[lst2[0]]:
        print('Yes')
    else:
        search_in_di(lst2[0], lst2[1], di)
        if g != 'Yes':
            print('No')
    g = ''
def search_in_di(a, b, c):
    global g
    for i in c[a]:
        if b in c[i]:
            if g != 'Yes':
                g = 'Yes'
                print('Yes')
                break
        else:
            search_in_di(i, b, c)
for i in range(int(input())):
    dict_inheritance(dict_complation(str(input())))
for i in range(int(input())):
    check_classes(di)