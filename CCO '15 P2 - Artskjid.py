#Bitmask dp and BFS 
#dp[v][mask] - is it possible to reach v with only the nodes in the mask

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    s, d, l = map(int, input().split())
    graph[s].append((d, l))

dp = [([-float('inf')] * (1<<n)) for _ in range(n)]
dp[0][1<<0] = 0
q = deque([(0, 1<<0)])
longest = -float('inf')

while q:
    v, mask = q.popleft()
    if v == n-1:
        longest = max(dp[v][mask], longest)
        
    for u, w in graph[v]:
        new_mask = mask | (1<<u)
        if dp[v][mask] + w > dp[u][new_mask] and new_mask != mask:
            q.append((u, new_mask))
            dp[u][new_mask] = dp[v][mask] + w

print(longest)

