import heapq

N, M = map(int, input().split())
island_cost = list(map(int, input().split()))
island_cost.insert(0, 0)  # Insert 0 at the start to make island_cost 1-indexed

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


priority_queue = []
for i in range(1, N+1):
    heapq.heappush(priority_queue, (-island_cost[i], i))



while priority_queue:
    current_cost, i = heapq.heappop(priority_queue)
    current_cost = -current_cost  
    for neighbor, cost in graph[i]:
        if current_cost - cost > island_cost[neighbor]:
            island_cost[neighbor] = current_cost - cost
            heapq.heappush(priority_queue, (-island_cost[neighbor], neighbor))

for i in range(1, N+1):
    print(island_cost[i])
