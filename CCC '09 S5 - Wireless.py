import math

m = int(input()) 
n = int(input())  
k = int(input())  

grid = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
    x, y, r, b = map(int, input().split())
    x -= 1
    y -= 1  

    for j in range(-r, r + 1):
        row = y + j
        if 0 <= row < m:
            spread = int(math.sqrt(r**2 - j**2))
            left = max(x - spread, 0)
            right = min(x + spread, n - 1)

            grid[row][left] += b
            if right + 1 < n:
                grid[row][right + 1] -= b


max_bitrate = 0
count = 0

for i in range(m):
    for j in range(1, n):
        grid[i][j] += grid[i][j - 1]

    for j in range(n):
        if grid[i][j] > max_bitrate:
            max_bitrate = grid[i][j]
            count = 1
        elif grid[i][j] == max_bitrate:
            count += 1

print(max_bitrate)
print(count)