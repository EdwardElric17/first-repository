m = []
new = []
n = 0
list = ''
while True:
    list = str(input())
    if list == 'end':
        break
    m.append([int(s) for s in list.split()])
    n += 1
    k = len(m[0])
for i in range(n):
    for j in range(k):
        if n == 0:
            print(m[0][j] + m[i][0] + m[i-1][j], end=' ')
        if i == n - 1 and j == k - 1:
            print(m[0][j] + m[i][0] + m[i-1][j] + m[i][j-1], end=' ')
        elif j == k - 1:
             print(m[i+1][j] + m[i][0] + m[i-1][j] + m[i][j-1], end=' ')
        elif i == n - 1:
            print(m[0][j] + m[i][j+1] + m[i-1][j] + m[i][j-1], end=' ')
        else:
            print(m[i+1][j] + m[i][j+1] + m[i-1][j] + m[i][j-1], end=' ')
    print()
