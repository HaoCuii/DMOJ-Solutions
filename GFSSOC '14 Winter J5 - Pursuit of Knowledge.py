from collections import deque

N, M, T = map(int, input().split())
adjacency_matrix = [[float('inf')] * (N + 1) for _ in range(N + 1)]
paths = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjacency_matrix[a][b] = 1
    paths[a].append(b)

for i in range(1, N + 1):
    queue = deque([(i, 0)])
    visited = set()
    while queue:
        node, dist = queue.popleft()
        if dist < adjacency_matrix[i][node]:
            adjacency_matrix[i][node] = dist
        for neighbor in paths[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)

Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())
    if adjacency_matrix[a][b] == float('inf'):
        print('Not enough hallways!')
    else:
        print(adjacency_matrix[a][b]*T)



