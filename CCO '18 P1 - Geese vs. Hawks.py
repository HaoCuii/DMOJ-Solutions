#dp[i][j] max total rivalry score using first i goose games and first j hawk games
n = int(input())
goose, hawk = [], []
s = list(input())
for i in range(n):
    goose.append([s[i]])
a = list(map(int,input().split()))
for i in range(n):
    goose[i].append(a[i])
t = list(input())
for i in range(n):
    hawk.append([t[i]])
b = list(map(int,input().split()))
for i in range(n):
    hawk[i].append(b[i])

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    res,score = goose[i][0],goose[i][1]
    for j in range(n):
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        if (res == 'W' and hawk[j][0] == "L" and score > hawk[j][1]) or (res == 'L' and hawk[j][0] == 'W' and score < hawk[j][1]):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+hawk[j][1]+score)

print(dp[-1][-1])

            




            

