'''
from collections import deque
for i in range(5):
    row_cube,col_cube = map(int,input().split())
    inputs = []
    largest_num, water = 0, 0

    for i in range(row_cube):
        x,y = input(),[]
        for j in x.split():
            y.append(int(j))
            if int(j) > largest_num:
                largest_num = int(j)
        inputs.append(y)

    cube_world = []

    for i in range(largest_num):
        layer = []
        for j in inputs:
            r = []
            for k in j:
                r.append(min(1, max(k-i,0)))
            layer.append(r)
        cube_world.append(layer)

    def bfs(grid,row,col):
        global water
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque([(row,col)])
        while queue:
            row,col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if  0 <= nr < row_cube and 0 <= nc < col_cube:
                    if grid[nr][nc] != 1:
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr,nc))
                else:
                    return
        water += 1

    for i in range(len(cube_world)):
        for j in range(len(cube_world[0])):
            for k in range(len(cube_world[0][0])):
                if cube_world[i][j][k] == 0:
                    bfs(cube_world[i],j,k)

    print(water)

'''

