with open("dataset_3363_2.txt", 'r') as inf:
    s = inf.readline()
l = str()
m = str()
i = 0
if s[len(s)-2].isdigit():
    while i <= len(s) - 3:
        j = 0
        if s[i+1].isdigit():
            m = s[i+1]
            if s[i+2].isdigit():
                m += s[i+2]
                j += 1
            l += s[i] * int(m)
        j += 1
        i += j
else:
    while i <= len(s) - 2:
        j = 0
        if i == len(s) - 2:
            m = s[i+1]
            l += s[i] * int(m)
            break
        if s[i+1].isdigit():
            m = s[i+1]
            if s[i+2].isdigit():
                m += s[i+2]
                j += 1
            l += s[i] * int(m)
        j += 1
        i += j
with open('file.txt', 'w') as ouf:
    ouf.write(l)
with open("file.txt", 'r') as inf:
    d = inf.readline()
print(d)