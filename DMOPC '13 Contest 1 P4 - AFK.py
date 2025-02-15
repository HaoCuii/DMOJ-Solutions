from collections import deque

a = int(input())
for _ in range(a):
    c,r = map(int,input().split())
    grid = []
    for i in range(r):
        grid.append(list(input()))

    queue = deque([])

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'C':
                queue.append((i,j,1))
                break

    visited = set()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    not_found = True
    while queue:
        r1,c1,l = queue.popleft()
        if l > 59:
            continue
        else:
            for i in directions:
                nr,nc = r1 + i[0],c1 + i[1]
                if 0 <= nr < r and 0 <= nc < c and (nr,nc) not in visited and grid[nr][nc] != 'X':
                    if grid[nr][nc] == 'W':
                        print(l)
                        queue = deque()
                        not_found = False
                        break
                    else:
                        visited.add((nr,nc))
                        queue.append((nr,nc,l+1))
    
    if not_found:
        print('#notworth')

