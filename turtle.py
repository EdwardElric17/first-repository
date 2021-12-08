m = []
c = [int(0), int(0)]
n = int(input())
for i in range(n):
    m = []
    m += [str(i) for i in input().split()]
    if m[0] == 'восток':
        c[0] += int(m[1])
    elif m[0] == 'запад':
        c[0] -= int(m[1])
    elif m[0] == 'север':
        c[1] += int(m[1])
    elif m[0] == 'юг':
        c[1] -= int(m[1])
print(c[0], end = ' ')
print(c[1])