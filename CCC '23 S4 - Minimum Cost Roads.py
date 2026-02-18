'''
editorial spam
sort edges in order of length then if it's a tie in order of cost 
construct new graph
for each edge connecting node u and v if it's < to the shortest length from u and v (in our new graph) we take it
find shortest length by running dijkstras
'''
import heapq

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
edges = []
for i in range(m):
    u,v,l,c = map(int,input().split())
    edges.append((l,c,u,v))

for l,c,u,v in sorted(edges):
    dist = [float('inf') for _ in range(n+1)]
    dist[u] = 0
    queue = [(0,u)]
    while queue:
        d,node = heapq.heappop(queue)
        if d > dist[node]:
            continue
        for new_node, newd, _, _ in graph[node]:
            if d + newd < dist[new_node]:
                dist[new_node] = d + newd
                heapq.heappush(queue, (d+newd, new_node))
    if l < dist[v]:
        graph[u].append((v,l,c,'yes'))
        graph[v].append((u,l,c,'fuh nah'))

ans = 0
for i in graph:
    for a,b,c,d in i:
        if d == 'yes':
            ans += c
print(ans)
    
