import heapq
n,a,b = map(int, input().split())
pq = []
heapq.heappush(pq, (a + b, 1, 1, True))
ans = 0 

for _ in range(n):
    cost, i, j, last = heapq.heappop(pq)
    ans += cost
    heapq.heappush(pq, (cost + b, i, j + 1, False))
    if last:
        heapq.heappush(pq, (cost + a, i + 1, j, True))

print(ans)
