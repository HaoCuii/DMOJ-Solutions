N,M,K = map(int,input().split())

grid = []

for i in range(N):
    l = list(input())
    grid.append(l)


a_pos = [[] for _ in range(N)]
b_pos = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'A':
            a_pos[i].append(j)
        elif grid[i][j] == 'B':
            b_pos[i].append(j)

from bisect import bisect_left

for i in range(N):
    for j in a_pos[i]:
        idx = bisect_left(b_pos[i], j)
        found = False
        if idx < len(b_pos[i]) and b_pos[i][idx] <= j + K:
            found = True
        if found:
            grid[i][j] = 'N'
        else:
            grid[i][j] = 'Y'

for i in range(N):
    for j in b_pos[i]:
        idx = bisect_left(a_pos[i], j)
        found = False
        if idx < len(a_pos[i]) and a_pos[i][idx] <= j - K:
            found = True
        if found:
            grid[i][j] = 'N'
        else:
            grid[i][j] = 'Y'

from bisect import bisect_right

for i in range(N):
    for j in b_pos[i]:
        idx = bisect_right(a_pos[i], j)
        found = False
        if idx > 0 and a_pos[i][idx - 1] >= j - K:
            found = True
        if found:
            grid[i][j] = 'N'
        else:
            grid[i][j] = 'Y'

for i in grid:
    print(''.join(i))

    

    