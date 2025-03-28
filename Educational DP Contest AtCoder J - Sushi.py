'''
dp[i][j][k] is number of operations at i ones, j twos, and k threes.
Start at 0,0,0 and work our way up filling up the dp table, then we make calls to find the expected operations
'''
n = int(input())
sushi = list(map(int, input().split()))

dp = [[[0.0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

for total in range(1, n+1):
    for i in range(total, -1, -1):
        for j in range(total - i, -1, -1):
            k = total - i - j
            res = n
            if i > 0:
                res += i * dp[i-1][j][k]
            if j > 0:
                res += j * dp[i+1][j-1][k]
            if k > 0:
                res += k * dp[i][j+1][k-1]
            dp[i][j][k] = res / (i + j + k)

print(dp[sushi.count(1)][sushi.count(2)][sushi.count(3)])



