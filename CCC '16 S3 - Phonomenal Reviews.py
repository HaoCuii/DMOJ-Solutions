'''
first compress the graph, remove all leaf nodes that aren't pho restaurants
The remaining graph must be visited fully, run diameter of tree 
'''

from collections import deque

n,m = map(int, input().split())
pho = set()
grid = [[] for _ in range(n)]
x = list(map(int,input().split()))
for i in range(m):
    pho.add(x[i])
for i in range(n-1):
    a,b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

q = deque([])
for i in range(n):
    if len(grid[i]) == 1 and i not in pho:
        q.append(i)
while q:
    u = q.popleft()
    grid[grid[u][0]].remove(u)
    if len(grid[grid[u][0]]) == 1 and grid[u][0] not in pho:
        q.append(grid[u][0])
    grid[u] = []
    n-= 1

def dfs(start):
    stack = [(start, -1, 0)]
    far_node, max_dist = start, 0
    while stack:
        node, parent, d = stack.pop()
        if d > max_dist:
            far_node, max_dist = node, d
        for v in grid[node]:
            if v != parent:
                stack.append((v, node, d + 1))
    return far_node, max_dist

farthest, _ = dfs(x[0])
_, diameter = dfs(farthest)

print(2*(n-1) - diameter)

    


