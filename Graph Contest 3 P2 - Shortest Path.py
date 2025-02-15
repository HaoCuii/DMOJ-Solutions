'''
import sys
import heapq
N, M= map(int,input().split())

graph = {}
inf = sys.maxsize

for i in range(M):
    city1,city2,shipping = map(int,input().split())
    try:
        graph[city1].append((city2,shipping))
    except KeyError:
        graph[city1] = [(city2,shipping)]

dist = [inf for _ in range(N + 1)]
dist[1] = 0
queue = [(0,1)]

while queue:
    distance, node = heapq.heappop(queue)
    if distance > dist[node]:
        continue
    for new_node,weight in graph.get(node,[]):
        new_dist = distance + weight
        if new_dist < dist[new_node]:
            dist[new_node] = new_dist
            heapq.heappush(queue,(dist[new_node],new_node))

print(dist[N])
'''

import sys
import heapq
N, M= map(int,input().split())

graph = {}
inf = float('inf')

for i in range(M):
    city1,city2,shipping = map(int,input().split())
    try:
        graph[city1].append((city2,shipping))
    except KeyError:
        graph[city1] = [(city2,shipping)]
    try:
        graph[city2].append((city1,shipping))
    except KeyError:
        graph[city2] = [(city1,shipping)]

dist = [inf for _ in range(N + 1)]
dist[1] = 0
queue = [(0,1)]

while queue:
    distance, node = heapq.heappop(queue)
    if distance > dist[node]:
        continue
    for new_node,weight in graph.get(node,[]):
        new_dist = distance + weight
        if new_dist < dist[new_node]:
            dist[new_node] = new_dist
            heapq.heappush(queue,(dist[new_node],new_node))

for i in range(1,N+1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])