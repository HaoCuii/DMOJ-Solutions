R,C = map(int,input().split())
graph = []
for i in range(R):
    graph.append(list(input()))

wall = False
for i in range(R):
    if graph[i][0] != '#' and not wall:
        graph[i][0] = 1
    else:
        graph[i][0] = 0
        wall = True

wall = False
for i in range(C):
    if graph[0][i] != '#' and not wall:
        graph[0][i] = 1
    else:
        graph[0][i] = 0
        wall = True

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '.':
            graph[i][j] = graph[i-1][j] + graph[i][j-1]
        elif graph[i][j] == '#':
            graph[i][j] = 0

print(graph[R-1][C-1] % (10**9 + 7))