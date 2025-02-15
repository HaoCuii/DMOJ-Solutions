from collections import deque
patients = list(map(int, input().split()))
blood = list(map(int, input().split()))

graph = graph = [[0] * 18 for _ in range(18)]

#Source to blood
for i in range(1,9):
    graph[0][i] = patients[i-1]  
#o- 
for i in range(9,17):
    graph[1][i] = float('inf')
#o+ 
for i in [10,12,14,16]:
    graph[2][i] = float('inf')
#A-
for i in [11,12,15,16]:
    graph[3][i] = float('inf')
#A+
for i in [12,16]:
    graph[4][i] = float('inf')
#B-
for i in range(13,17):
    graph[5][i] = float('inf')
#B+
for i in [14,16]:
    graph[6][i] = float('inf')
#AB-
for i in [15,16]:
    graph[7][i] = float('inf')

graph[8][16] = float('inf')

#Blood to sink
for i in range(9,17):
    graph[i][17] = blood[i-9]

def bfs(s,t,parent):
    visited = [False]*18
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        for index,val in enumerate(graph[v]):
            if visited[index] == False and val > 0:
                q.append(index)
                visited[index] = True
                parent[index] = v
                if index == t:
                    return True
    return False

def ford_fulkerson(source,sink):
    parent = [-1]*18
    max_flow = 0
    while bfs(source,sink,parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow,graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
    
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

print(ford_fulkerson(0,17))