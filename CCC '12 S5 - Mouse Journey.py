import tensorflow as tf
'''
R,C = map(int,input().split())
lab = [['x']*C for _ in range(R)] 

for i in range(int(input())):
    r,c = map(int,input().split())
    lab[r-1][c-1] = 0

b = False
for i in range(len(lab)):
    if lab[i][0] == 0:
        b = True
    if b:
        lab[i][0] = 0
    else:
        lab[i][0] = 1

b = False
for i in range(len(lab[0])):
    if lab[0][i] == 0:
        b = True
    if b:
        lab[0][i] = 0
    else:
        lab[0][i] = 1

for i in range(len(lab)):
    for j in range(len(lab[0])):
        if lab[i][j] == 'x':
            lab[i][j] = lab[i-1][j] + lab[i][j-1]

print(lab[R-1][C-1])
'''

