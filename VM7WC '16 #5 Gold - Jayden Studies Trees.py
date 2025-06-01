import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, parent):
    far_node, max_dist = node, 0
    for neighbor in graph[node]:
        if neighbor != parent:
            next_node, dist = dfs(neighbor, node)
            if dist + 1 > max_dist:
                far_node, max_dist = next_node, dist + 1
    return far_node, max_dist

farthest, _ = dfs(1, -1)
_, diameter = dfs(farthest, -1)

print(diameter)
