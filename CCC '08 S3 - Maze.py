import collections
inp = int(input())
for i in range(inp):
    x = int(input())
    y = int(input())
    bool = False
    graph = []
    for j in range(x):
        z = input()
        graph.append(list(z))
    visited = set()
    queue = collections.deque([['',0,0]])
    while queue:
        current_path, row, col= queue.popleft()

        if (row+1,col+1) == (x,y) and graph[row][col] != '*':
            print(len(current_path)+1)
            bool = True
            break

        if graph[row][col] == '+':
            directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
            for i in directions:
                new_row, new_col = row+i[0], col+i[1]
                if -1 < new_row < x and -1 < new_col < y and (new_row,new_col) not in visited:
                    queue.append([current_path+graph[new_row][new_col],new_row,new_col])
                    visited.add((new_row,new_col))

        elif graph[row][col] == '-':

            directions = [[0, 1],[0, -1]]
            for i in directions:
                new_row, new_col = row+i[0], col+i[1]    
                if -1 < new_row < x and -1 < new_col < y and (new_row,new_col) not in visited:
                    queue.append([current_path+graph[new_row][new_col],new_row,new_col])
                    visited.add((new_row,new_col))

        elif graph[row][col] == '|':

            directions = [[1, 0],[-1, 0]]
            for i in directions:
                new_row, new_col = row+i[0], col+i[1]    
                if -1 < new_row < x and -1 < new_col < y and (new_row,new_col) not in visited:
                    queue.append([current_path+graph[new_row][new_col],new_row,new_col])
                    visited.add((new_row,new_col))
    if not bool:
        print('-1')
    
        
