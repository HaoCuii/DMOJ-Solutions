#dp[mask] - how many ways to pair that mask
n = int(input())
compat = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (1<<n)
dp[0] = 1

for mask in range(1<<n):
    m = mask.bit_count()
    if m == n:
        print(dp[mask] % (10**9 + 7)) 
        break
    for w in range(n):
        if (mask & (1 << w)) == 0 and compat[m][w]:
            dp[mask | (1 << w)] += dp[mask]  



 