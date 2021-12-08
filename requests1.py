import requests
t = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
i = 0
while True:
    r = requests.get(t)
    g = r.text
    print(g)
    t = 'https://stepic.org/media/attachments/course67/3.6.3/' + str(g)
    if g[0] == 'W' and g[1] == 'e':
        break