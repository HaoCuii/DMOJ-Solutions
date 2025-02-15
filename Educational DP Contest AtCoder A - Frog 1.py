n = int(input())
l = list(map(int,input().split()))
dp = [float('inf') for _ in range(n)]
dp[0] = 0
dp[1] = abs(l[0] - l[1])

for i in range(n-2):

    if dp[i] + abs(l[i] - l[i+2]) < dp[i+1] + abs(l[i+1]- l[i+2]):
        dp[i+2] = dp[i] + abs(l[i] - l[i+2])
    else:
        dp[i+2] = dp[i+1] + abs(l[i+1] - l[i+2])    

print(dp[-1])