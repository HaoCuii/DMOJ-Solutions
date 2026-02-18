'''
dp[i] = max[dp[i-1],sum[i,i]+dp[i-2], sum[i,i-1]+dp[i-3]... sum[i,i-k] + dp[i-k-1]]
fix k+1 different starting terms
'''

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    if k == n:
        print(sum(x for x in v if x > 0))
        continue
    ans = 0
    for start in range(k+1):
        nk = []
        for i in range(1,n):
            if start + i < n:
                nk.append(v[start+i])
            else:
                nk.append(v[start+i-n])
        psa = [nk[0]]
        for i in range(1,n-1):
            psa.append(psa[i-1] + nk[i])

        dp = [0 for _ in range(n-1)]
        for i in range(n-1):
            best = 0
            if i >= 1:
                best = dp[i - 1]
            for j in range(1, k + 1): 
                if i - j + 1 < 0:
                    break
                if i - j + 1 == 0:
                    seg = psa[i]
                else:
                    seg = psa[i] - psa[i - j]
                if i - j - 1 >= 0:
                    prev = dp[i - j - 1]
                else:
                    prev = 0             
                best = max(best, prev + seg)
            dp[i] = best
        ans = max(ans,dp[-1])
    print(ans)

