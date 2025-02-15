import sys
sys.setrecursionlimit(100000)

def dfs(node, visited, length):  
    if dp[node] != -1: 
        return dp[node]
    max_length = 0
    for neighbor in paths[node]:
            max_length = max(max_length, 1+ dfs(neighbor, visited, length + 1))
    dp[node] = max_length
    return max_length

N, M = map(int, input().split())
paths = [[] for _ in range(N + 1)]
dp = [-1] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    paths[a].append(b)

longest = 0
for i in range(1, N + 1):
    visited = set()
    p = dfs(i, visited, 0)
    longest = max(longest,p)

print(longest)
