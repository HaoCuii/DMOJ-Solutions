import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
edge = []

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))
    edge.append(c)

dist = [float('inf')] * m
queue = []

for next_node, edge_idx in graph[1]:
    dist[edge_idx] = edge[edge_idx]
    heapq.heappush(queue, (edge[edge_idx], next_node, edge_idx))

while queue:
    cost, node, e = heapq.heappop(queue)

    if node == n:
        print(cost)
        break

    if cost > dist[e]:
        continue 
    for new_node, new_e in graph[node]:
        new_cost = cost + abs(edge[e] - edge[new_e])
        if new_cost < dist[new_e]:
            dist[new_e] = new_cost
            heapq.heappush(queue, (new_cost, new_node, new_e))

