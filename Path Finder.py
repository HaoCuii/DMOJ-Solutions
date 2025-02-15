from collections import deque
import sys
input = sys.stdin.readline

row, col, K = map(int, input().split())
walls = set()
left_bottom = set()

for i in range(K):
    a, b = map(int, input().split())
    if a == row or b == 1:
        left_bottom.add((a,b))
    walls.add((a, b))

visited = set()

for (br,bc) in left_bottom:
    if (br,bc) not in visited:
        queue = deque([(br, bc)])
        while queue:
            r,c = queue.popleft()
            if c == col or r == 1:
                print('NO')
                sys.exit()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in walls and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

print('YES')
