l = set()
p = set()
n = int(input())
m = []
for i in range(n):
    l.add(input().lower())
k = int(input())
for i in range(k):
    m += ([str(s) for s in input().lower().split()])
for i in m:
    if i not in l:
        p.add(i)
for i in p:
    print(i)