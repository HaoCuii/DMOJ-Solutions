from collections import deque
import sys
n,h = map(int,input().split())
queue = deque([(0,0)])
field = []
for i in range(n):
    field.append(list(map(int,input().split())))

vis = set([(0,0)])

while queue:
    r,c = queue.popleft()
    if (r,c) == (n-1,n-1):
        print('yes')
        sys.exit()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for (a,b) in directions:
        nr,nc = r+a,c+b
        if 0 <= nr < n and 0 <= nc < n and abs(field[nr][nc] - field[r][c]) <= h and (nr,nc) not in vis:
            vis.add((nr,nc))
            queue.append((nr,nc))

print('no')
