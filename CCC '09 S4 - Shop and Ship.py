import sys
from collections import deque
input = sys.stdin.readline

cities = int(input())
routes = int(input())

graph = [[float('inf')] * (cities + 1) for _ in range(cities + 1)]
dist = [float('inf') for _ in range(cities + 1)]

queue = deque()
for _ in range(routes):
    city1, city2, weight = map(int,input().split())
    graph[city1][city2] = weight
    graph[city2][city1] = weight

costs = int(input())

for _ in range(costs):
    city, cost = map(int,input().split())
    dist[city] = cost
    queue.append([city, cost])

end_node = int(input())

while queue:
    node, distance = queue.popleft()
    for i in range(1, cities + 1):
        if graph[node][i] + distance < dist[i]:
            dist[i] = graph[node][i] + distance
            queue.append((i,graph[node][i]+distance))

print(dist[end_node])
