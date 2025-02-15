import heapq
N,m = map(int,input().split())
graph = [[] for _ in range(N)]

for _ in range(m):
    a,b,l = map(int,input().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

dist = [float('inf') for _ in range(N)]
queue = [(0,0)]
dist[0] = 0
while queue:
    l,n = heapq.heappop(queue)
    for i in graph[n]:
        if l + i[1] < dist[i[0]]:
            dist[i[0]] = l + i[1]
            heapq.heappush(queue,(l + i[1],i[0]))

all_dist = []

for i in range(len(dist)):
    dist1 = [float('inf') for _ in range(N)]
    queue = [(dist[i],i)]
    dist1[i] = dist[i]
    while queue:
        l,n = heapq.heappop(queue)
        for j in graph[n]:
            if l + j[1] < dist1[j[0]]:
                dist1[j[0]] = l + j[1]
                heapq.heappush(queue,(l + j[1],j[0]))
    all_dist.append(dist1[n-1])

print(max(all_dist))
   