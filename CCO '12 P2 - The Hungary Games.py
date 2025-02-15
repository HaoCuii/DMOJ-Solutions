import heapq
nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes+1)]

for _ in range(edges):
    a,b,l = map(int,input().split())
    graph[a].append([b,l])

dist = [float('inf') for _ in range(nodes + 1)]
queue = [(0,1)]

while queue:
    l,n = heapq.heappop(queue)
    if l > dist[n]:
        continue
    for i in graph[n]:
        if l + i[1] < dist[i[0]]:
            dist[i[0]] = l + i[1]
            heapq.heappush(queue,(l + i[1],i[0]))

shortest = dist[nodes]

dist = [[float('inf'),(float('inf'))] for _ in range(nodes + 1)]
queue = [(0,1)]

while queue:
    l,n = heapq.heappop(queue)
    val = -1
    for i in graph[n]:
        if i[0] == nodes:
            val = shortest
        if l + i[1] < dist[i[0]][0] and l + i[1]:
            if dist[i[0]][0] > val:
                dist[i[0]][1] = dist[i[0]][0]
            dist[i[0]][0] = l + i[1]
            heapq.heappush(queue,(l + i[1],i[0]))
        elif l + i[1] < dist[i[0]][1] and l + i[1] > val:
            dist[i[0]][1] = l + i[1]
            heapq.heappush(queue,(l + i[1],i[0]))

if dist[nodes][1] == float('inf'):
    print(-1)
else:
    print(dist[nodes][1])
print(dist)
