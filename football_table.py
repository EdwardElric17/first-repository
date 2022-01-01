n = int(input())
all = []
m02 = []
m02_1 = []
cout_wins = {}
cout_draw = {}
cout_loss = {}
cout_points = {}
cout_games = {}
k = 0
for i in range(n):
    all.append([str(i) for i in input().split(';')])
for i in range(n):
    for j in range(4):
        if j == 0 or j == 2:
            m02.append(all[i][j])
            cout_wins[all[i][j]] = 0
            cout_draw[all[i][j]] = 0
            cout_loss[all[i][j]] = 0
            cout_points[all[i][j]] = 0
            cout_games[all[i][j]] = 0
for i in range(n):
    if int(all[i][1]) > int(all[i][3]):
        cout_wins[all[i][0]] += 1
        cout_loss[all[i][2]] += 1
    elif int(all[i][1]) < int(all[i][3]):
        cout_wins[all[i][2]] += 1
        cout_loss[all[i][0]] += 1
    elif int(all[i][1]) == int(all[i][3]):
        cout_draw[all[i][0]] += 1
        cout_draw[all[i][2]] += 1
for key in cout_wins.keys():
    m02_1.append(key) 
for i in m02:
    if i in cout_games:
        cout_games[i] += 1
for key in cout_points.keys():
    cout_points[key] += cout_wins[key] * 3
    cout_points[key] += cout_draw[key]
for i in m02_1:
    print(i + ':' + str(cout_games[i]) + ' ' + str(cout_wins[i]) + ' ' + str(cout_draw[i]) + ' ' + str(cout_loss[i]) + ' ' + str(cout_points[i]))