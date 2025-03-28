import sys
sys.setrecursionlimit(9999)
c, r, d = map(int, input().split())
sorted_edges = []
for i in range(r):
    a, b, l = map(int, input().split())
    sorted_edges.append((l, a, b))

sorted_edges.sort(reverse=True)

cities = [int(input()) for _ in range(d)]


Parent = [i for i in range(c + 1)]
Rank = [0] * (c + 1)

def find(x):
    if Parent[x] != x:
        Parent[x] = find(Parent[x])
    return Parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if x_root != y_root:
        if Rank[x_root] < Rank[y_root]:
            Parent[x_root] = y_root
        elif Rank[x_root] > Rank[y_root]:
            Parent[y_root] = x_root
        else:
            Parent[y_root] = x_root
            Rank[x_root] += 1

maxst = [[] for _ in range(c + 1)]
for l, a, b in sorted_edges:
    if find(a) != find(b):
        union(a, b)
        maxst[a].append((b, l))
        maxst[b].append((a, l))
    

min_weight = {}
    
def dfs(u, parent_node, current_min):
    min_weight[u] = current_min
    for v, w in maxst[u]:
        if v != parent_node:
            dfs(v, u, min(current_min, w))
    
dfs(1, -1, float('inf'))
    
smallest = float('inf')
for city in cities:
    smallest = min(smallest, min_weight[city])
    
print(smallest)

