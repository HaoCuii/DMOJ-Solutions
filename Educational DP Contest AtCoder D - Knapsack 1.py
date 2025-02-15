N,W = map(int,input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]
items = []

for i in range(N):
    items.append(list(map(int,input().split())))

for i in range(N+1):
    for j in range(W + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif j - items[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j],dp[i - 1][j - items[i - 1][0]] + items[i - 1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])