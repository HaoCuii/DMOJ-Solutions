edge = int(input())
frac = []
for i in range(edge):
    l = list(map(int,input().split()))
    frac.append(l)

patt = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
patt2 = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def threebythree(r, c, frac):
    one, zero = 0, 0
    try:
        for i in range(3):
            for j in range(3):
                if frac[r+i][c+j] == patt[i][j]:
                    one += 1
                if frac[r+i][c+j] == patt2[i][j]:
                    zero += 1
    except IndexError:
        return 4
    
    if one == 9:
        return 2
    elif zero == 9:
        return 3
    else:
        return False

def recursion(r,c,frac,edge,depth):
    print(frac)
    print('nigger')
    global count2
    global cnt
    new_frac = [[] for _ in range(edge//3)]
    count = 0
    for i in range(r, edge, 3):
        for j in range(c, edge, 3):
            tbt = threebythree(i,j,frac)
            if tbt == 2:
                new_frac[count].append(1)
            elif tbt == 3:
                new_frac[count].append(0)
            elif tbt == False:
                new_frac[count].append(2)
        count += 1
    if new_frac == [[0]]:
        count2 = 0
        return
    if new_frac == [[]]:
        count2 = depth
        return
    if new_frac == []:
        count2 = depth
        return
    f = False
    for k in new_frac:
        for l in k:
            if l == 1:
                f = True
                break
    if f:
        for i in range(3):
            for j in range(3):
                recursion(i,j,new_frac,int(edge/3),depth+1)
                if count2 > cnt:
                    cnt = count2
    else:
        count2 = depth
        return
   
cases = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

cnt = 0

for (i,j) in cases:
    count2 = 0
    recursion(i,j,frac,edge,0)
    if count2 > cnt:
        cnt = count2


if cnt == 0:
    print(0)
else: 
    print(3**cnt)