cols,rows = input().split()
final_cols,final_rows = input().split()
rows,cols,final_cols,final_rows = int(rows),int(cols),int(final_cols),int(final_rows)
path_len = 0
paths = []
def dfs(rows,cols,visited,path_len):
    if 0 < rows < 9 and 0 < cols < 9 and (rows,cols) not in visited:
        if (rows,cols) == (final_rows,final_cols):
            paths.append(path_len)
        else:
            if path_len > 5:
                return
            else:
                visited.append((rows,cols))
                dfs(rows+1,cols-2,visited.copy(),path_len+1)
                dfs(rows+1,cols+2,visited.copy(),path_len+1)
                dfs(rows-1,cols-2,visited.copy(),path_len+1)
                dfs(rows-1,cols+2,visited.copy(),path_len+1)
                dfs(rows+2,cols-1,visited.copy(),path_len+1)
                dfs(rows+2,cols+1,visited.copy(),path_len+1)
                dfs(rows-2,cols-1,visited.copy(),path_len+1)
                dfs(rows-2,cols+1,visited.copy(),path_len+1)
                path_len += 1
visited = []
dfs(rows,cols,visited,path_len)
print(sorted(paths)[0])
