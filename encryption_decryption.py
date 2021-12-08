alphabet_1 = input()
alphabet_2 = input()
list_1 = input()
list_2 = input()
d_1 = {}
d_2 = {}
m_1 = []
m_2 = []
m_3 = []
m_4 = []
for i in range(len(alphabet_1)):
    d_1[alphabet_1[i]] = []
    d_1[alphabet_1[i]] = alphabet_2[i]
for i in range(len(list_1)):
    m_1.append(list_1[i])
    m_2.append(d_1[m_1[i]])
for i in range(len(alphabet_2)):
    d_2[alphabet_2[i]] = []
    d_2[alphabet_2[i]] = alphabet_1[i]
for i in range(len(list_2)):
    m_3.append(list_2[i])
    m_4.append(d_2[m_3[i]])
for i in m_2:
    print(i, end='')
print()
for i in m_4:
    print(i, end='')

