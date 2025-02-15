n,k = map(int,input().split())
l = list(map(int,input().split()))
dp = [float('inf') for _ in range(n)]

dp[0] = 0
if n-k < 0:
     s = n
else:
     s = n-k
for i in range(s):
    dp[i] = abs(l[0] - l[i])


for i in range(s):
    shortest = float('inf')
    if i+k < len(l):
        for j in range(k):
                if dp[i+j] + abs(l[i+j] - l[i+k]) < shortest: 
                    shortest = dp[i+j] + abs(l[i+j] - l[i+k])
        dp[i+k] = shortest

print(dp[-1])