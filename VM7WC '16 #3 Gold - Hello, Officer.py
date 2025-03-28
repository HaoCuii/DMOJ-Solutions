import heapq

n,m,b,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

dist = [float('inf') for _ in range(n+1)]
dist[b] = 0
queue = [(0,b)]

while queue:
    distance,node = heapq.heappop(queue)
    if distance > dist[node]:
        continue
    for new,weight in graph[node]:
        new_dist = distance + weight
        if new_dist < dist[new]:
            dist[new] = new_dist
            heapq.heappush(queue,(dist[new],new))

for i in range(q):
    x = int(input())
    if dist[x] == float('inf'):
        print(-1)
    else:
        print(dist[x])
