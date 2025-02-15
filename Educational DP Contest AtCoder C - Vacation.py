import sys
N = int(input())
dp = [[0]*3 for _ in range(N)]
dic = {'a':0,'b':1,'c':2}
dp[0] = list(map(int, sys.stdin.readline().split()))
for i in range(1,N):
    a,b,c = map(int,input().split())
    dp[i][0],dp[i][1],dp[i][2] = max(dp[i-1][1],dp[i-1][2])+a,max(dp[i-1][0],dp[i-1][2])+b,max(dp[i-1][1],dp[i-1][0])+c

print(sorted(dp[-1])[2])