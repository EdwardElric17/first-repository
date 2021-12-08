s = str(input())
j = len(s) - 1
a = 1 
c = str('')
for i in range(0, j+1):
    if i == j:
        c += s[i] + str(a)
    elif s[i] == s[i+1]:
        a += 1
    elif s[i] != s[i+1]:
        c += s[i] + str(a)
        a = 1
print(c)