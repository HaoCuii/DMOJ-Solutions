from collections import deque

def recurse(a,b,c,d):
    global queue
    moves = [
        (a >= 1 and d >= 1, a - 1, b, c, d - 1),
        (a >= 1 and b >= 1 and c >= 1 and d >= 1, a - 1, b - 1, c - 1, d - 1),
        (a >= 2 and b >= 1 and d >= 2, a - 2, b - 1, c, d - 2),
        (b >= 3, a, b - 3, c, d),
        (c >= 2 and d >= 1, a, b, c - 2, d - 1)
    ]
    base = True
    for condition,a2,b2,c2,d2 in moves:
        if condition:
            base = False
    if base:
        queue.append((a,b,c,d))
        return

    for condition,a2,b2,c2,d2 in moves:
        if condition and (a2,b2,c2,d2) not in vis:
            vis.add((a2,b2,c2,d2))
            recurse(a2,b2,c2,d2)

n = int(input())
for i in range(n):
    nukit = list(map(int,input().split()))
    positions = []
    for i in range(nukit[0]+1):
        ii = []
        for j in range(nukit[1]+1):
            jj = []
            for k in range(nukit[2]+1):
                kk = []
                for l in range(nukit[3]+1):
                    kk.append(False)
                jj.append(kk)
            ii.append(jj)
        positions.append(ii)

    queue = deque([])
    vis = set()
    recurse(nukit[0],nukit[1],nukit[2],nukit[3])
    vis = set()
    directions = [[2, 1, 0, 2], [1, 1, 1, 1], [0, 0, 2, 1], [0, 3, 0, 0], [1, 0, 0, 1]]

    while queue:
        (a,b,c,d) = queue.popleft()
        for [aa,bb,cc,dd] in directions: 
            if a+aa <= nukit[0] and b+bb <= nukit[1] and c+cc <= nukit[2] and d+dd <= nukit[3]:
   
                if not positions[a][b][c][d] and not positions[a+aa][b+bb][c+cc][d+dd]:
                    positions[a+aa][b+bb][c+cc][d+dd] = True    
                    vis.add(((a+aa,b+bb,c+cc,d+dd)))
                    queue.append((a+aa,b+bb,c+cc,d+dd))
                elif positions[a][b][c][d] and not positions[a+aa][b+bb][c+cc][d+dd]:
                    vis.add((a+aa,b+bb,c+cc,d+dd))
                    queue.append((a+aa,b+bb,c+cc,d+dd))

    if positions[nukit[0]][nukit[1]][nukit[2]][nukit[3]]:
        print('Patrick')
    else:
        print('Roland')







