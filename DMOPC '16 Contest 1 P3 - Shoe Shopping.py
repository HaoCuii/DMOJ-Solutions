n = int(input())
prices = list(map(float, input().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 0 

for i in range(n):
    dp[i + 1] = min(dp[i + 1], dp[i] + prices[i])
    
    if i + 1 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + prices[i] + prices[i + 1] - min(prices[i], prices[i + 1]) * 0.5)
    
    if i + 2 < n:
        dp[i + 3] = min(dp[i + 3], dp[i] + prices[i] + prices[i + 1] + prices[i + 2] - min(prices[i], prices[i + 1], prices[i + 2]))

print(round(float(dp[n]), 1))