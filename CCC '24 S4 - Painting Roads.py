import sys
sys.setrecursionlimit(500000)
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
road_plan = []

for i in range(M):
    a,b = map(int,input().split())
    road_plan.append((a,b))
    graph[a].append((b,i))
    graph[b].append((a,i))

Parent = [i for i in range(N+1)]
Rank = [0] * (N + 1)
def find(x):
    if Parent[x] != x:
        return find(Parent[x])
    else:
        return x   
    
def union(x,y):
    x_root, y_root =  find(y), find(x)
    if Rank[x_root] < Rank[y_root]:
        Parent[x_root] = y_root
    elif Rank[x_root] > Rank[y_root]:
        Parent[y_root] = x_root
    else:
        Parent[y_root] = x_root
        Rank[x_root] += 1


st = []
visited = set()
def dfs(node,rank):
    for (neighbour,c) in graph[node]:
        if find(neighbour) != find(node):
            union(node,neighbour)
            st.append((c,node,neighbour,rank))
            visited.add(neighbour)
            dfs(neighbour,rank+1)

for i in range(1,N+1):
    if i not in visited:
        dfs(i,1)

for i in st:
    a,b,c,d = i
    if d % 2 == 0:
        road_plan[a] = 'R'
    else:
        road_plan[a] = 'B'

for i in range(len(road_plan)):
    if road_plan[i] not in ['R','B']:
        road_plan[i] = 'G'

print(''.join(road_plan))