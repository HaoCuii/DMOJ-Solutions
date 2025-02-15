N = int(input())

grid = [['0' for _ in range(N)] for _ in range(N)]

for i in range(2,N,5):
    for j in range(N):
        grid[i][j] = '1'

if N % 5 == 1:
    for i in range(1,N,3):
        grid[N-3][i] = '1'
        if i+1 < N:
            grid[N-3][i+1] = '1'
elif N % 5 == 2:
    for i in range(N-1):
        grid[N-3][i] = '1'
    for i in range(N//10):
        if (i*5) - 5 >= 0 and (i*5) + 5 <= N:
            grid[N-3][(i*5 - 1)] = '0'

for i in grid:
    print(' '.join(i))

        