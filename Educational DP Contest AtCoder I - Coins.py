'''
dp[i] is the probability of getting i heads 
iterate backwards 
the probability at i will be the current probability at i and then getting a tails + the current probability at i-1 * getting a head
'''

n = int(input())

coins = list(map(float, input().split()))

dp = [0] * (n + 1)
dp[0] = 1

for coin in range(n):
    heads = coins[coin]
    for i in range(coin + 1, -1, -1):
        if i > 0:
            dp[i] = dp[i - 1] * heads + dp[i] * (1 - heads)
        else:
            dp[i] = dp[i] * (1 - heads)

total = 0
for i in range(1,n+1):
    if i > n/2:
        total += dp[i]
print(total)