#Multisource Dijkstras from printers not covered by the sprinkler
import heapq
n,m,k,t = map(int,input().split())
non_source = set(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

pq = []
dist = [float('inf') for _ in range(n+1)]
for i in range(1,n+1):
    if i not in non_source:
        dist[i] = 0
        heapq.heappush(pq,(0,i))

while pq:
    cost,v = heapq.heappop(pq)
    if cost > dist[v]:
        continue
    for u,w in graph[v]:
        if  cost + w < dist[u]:
            dist[u] = cost + w
            heapq.heappush(pq,(dist[u],u))

ans = ['0' for _ in range(n)]
for i in range(1,n+1):
    if dist[i] > t:
        ans[i-1] = '1'

print(''.join(ans))


