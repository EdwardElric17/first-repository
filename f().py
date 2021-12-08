n = int(input())
mn = {}
for i in range(n):
    xi = int(input())
    if xi in mn:
        print(mn[xi])
    else:
        mn[xi] = f(xi)
        print(mn[xi])
    
