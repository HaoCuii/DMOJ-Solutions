N,K = map(int,input().split())
grid = [['' for _ in range(N)] for _ in range(N)]
largest_non_diagonal = 0

for i in range(K):
    grid[i][i] =  N**2-i
    largest_non_diagonal = N**2-i
for i in range(N):
    if grid[N-1][i] == '':
        grid[N-1][i] = largest_non_diagonal-(i+1)
c = 1
for i in range(N):
    for j in range(N):
        if grid[i][j] == '':
            grid[i][j] = c
            c += 1

for i in grid:
    print(' '.join(map(str,i)))