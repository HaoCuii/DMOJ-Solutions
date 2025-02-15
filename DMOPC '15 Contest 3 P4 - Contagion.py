import heapq

N = int(input())

graph = [[] for _ in range(N)]
cities = []

for i in range(N):
    a,b = map(int,input().split())
    cities.append((a,b))

X = int(input())-1
Q = int(input())

queries = []
for i in range(Q):
    queries.append((int(input()),i))
queries = sorted(queries)
#monkey the luffy
for i in range(0, N):
    for j in (range(i+1,N)):
        dist = (cities[i][0] - cities[j][0])**2 +  (cities[i][1] - cities[j][1])**2
        graph[i].append((j,dist))
        graph[j].append((i,dist))

dist = [float('inf') for _ in range(N)]
dist[X] = 0
queue = [(0,X)]

while queue:
    current_distance, node = heapq.heappop(queue)
    if current_distance > dist[node]:
        continue
    for neighbor, weight in graph[node]:
        new_distance = current_distance + weight
        if new_distance < dist[neighbor]:
            dist[neighbor] = new_distance
            heapq.heappush(queue, (new_distance, neighbor))

dist = sorted(dist)
out = []

low = 0
for target,i in queries:
    if target >= dist[-1]:
        out.append((i,N))
    else:
        low, high = low, N - 1
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if dist[mid] <= target:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append((i,result+1))

for i,o in sorted(out):
    print(o)
