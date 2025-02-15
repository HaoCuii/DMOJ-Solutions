s, n = int(input()), int(input())
d = sorted([int(input()) for i in range(n)])
dp = [float('inf')] *(s+1)
dp[0] = 0

for i in range(1,s+1):
    for j in d:
        if i - j >= 0:
            dp[i] = min(dp[i],1+dp[i-j])

print(dp[-1])