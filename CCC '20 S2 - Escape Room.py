import sys
from collections import deque

row1, col1 = int(input()), int(input())
grid = {}

for i in range(row1):
    x = sys.stdin.readline().split()
    for j in range(len(x)):
        if x[j] not in grid:
            grid[x[j]] = []
        grid[x[j]].append([i + 1, j + 1])

queue = deque([(row1, col1)])
bool_var = False

while queue:
    row, col = queue.popleft()
    if (row, col) == (1, 1):
        print('yes')
        sys.exit()
    if grid.get(str(row*col)):
        counter = 0
        for i in grid[str(row * col)]:
                if i != 'Visited':
                    queue.extend([(i[0], i[1])])
                    grid[str(row*col)][counter] = 'Visited'
                    counter += 1
print('no')