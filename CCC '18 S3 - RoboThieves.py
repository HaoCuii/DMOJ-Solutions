row, col = input().split()
row, col = int(row), int(col)
grid,path_len,conveyers = [],{},{'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
for i in range(row):
    grid.append(list(input()))
visited = set()

def conveyer(grid,row,col,m):
    if grid[row][col] in ['U','D','L','R']:
        r, c = row+conveyers[grid[row][col]][0],col+conveyers[grid[row][col]][1]
        if -1 < r < len(grid) and -1 < c < len(grid[0]) and grid[r][c] != 'W':
            if (r,c) not in visited:
                visited.add((r,c))
                new_row, new_col,m = conveyer(grid,r,c,m+1)
                return new_row,new_col,m
            else:
                return row,col,0
    return row,col,m
        
def bfs(grid,row,col):
    if (row,col) not in visited:
        queue = [[row,col,0]]
        while queue:
            current_path  = queue.pop(0)
            row, col, steps = current_path[0],current_path[1],current_path[2]
            if grid[row][col] == ".":
                path_len[(row,col)] = steps
            directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
            for i in directions:
                new_row, new_col = row+i[0], col+i[1]
                if -1 < new_row < len(grid) and -1 < new_col < len(grid[0]) and (new_row,new_col) not in visited and grid[new_row][new_col] != 'W':
                    visited.add((new_row,new_col))
                    if grid[new_row][new_col] in ['U','D','L','R']:
                        new_row,new_col,m = conveyer(grid,new_row,new_col,0)
                        if m == 0:
                            queue.append([row,col,steps])
                        else:
                            queue.append([new_row,new_col,steps+1])
                    else:
                        queue.append([new_row,new_col,steps+1])

def cameras(grid,row,col):
    queue = [[row,col,0],[row,col,1],[row,col,2],[row,col,3]]
    while queue:
        current_path  = queue.pop(0)
        row, col, index= current_path[0],current_path[1],current_path[2]
        directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        new_row, new_col = row+directions[index][0], col+directions[index][1]
        if -1 < new_row < len(grid) and -1 < new_col < len(grid[0]) and grid[new_row][new_col] != 'W':
            if grid[new_row][new_col] not in ['U','D','L','R']:
                visited.add((new_row,new_col))
            queue.append([new_row,new_col,index])
  
for i in range(row):
    for j in range(col):
        if grid[i][j] == 'S':
            start_row,start_col = i,j
        elif grid[i][j] == 'C':
            visited.add((i,j))
            cameras(grid,i,j)
bfs(grid, start_row, start_col)
for i in range(row):
    for j in range(col):
        if grid[i][j] == '.':
            try:
                print(path_len[(i,j)])
            except KeyError:
                print(-1)