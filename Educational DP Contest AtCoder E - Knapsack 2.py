N, W = map(int, input().split())
items = []
total = 0
for i in range(N):
    a, b = map(int, input().split())
    items.append((a, b))
    total += b

dp = [[float('inf') for _ in range(total+1)] for i in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    w,v = items[i-1]
    for j in range(total+1):
        if j-v >= 0:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-v] + w)
        else:
            dp[i][j] = dp[i-1][j]

for j in range(total,-1,-1):
    if dp[N][j] <= W:
        print(j)
        break