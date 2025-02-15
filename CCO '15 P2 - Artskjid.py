import sys

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dfs(node, adj, visited, stack):
    visited[node] = True

    for neighbor, _ in adj[node]: 
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, stack)
    
    stack.append(node)

stack = []
visited = [False] * N

for i in range(N):
    if not visited[i]:
        dfs(i, graph, visited, stack)

dist = [-float('inf')] * N
dist[0] = 0 

while len(stack) > 0: 
    node = stack.pop()
    for neighbor, cost in graph[node]: 
        if dist[neighbor] < dist[node] + cost: 
            dist[neighbor] = dist[node] + cost

print(dist[-1])
