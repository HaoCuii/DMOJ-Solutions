length = int(input())
seq = list(map(int, input().split()))

dp = [1] * length

for i in range(1, length):
    sub = []
    for j in range(i):
        if seq[j] < seq[i]:
            sub.append(dp[j])
    if sub:
        dp[i] = 1 + max(sub)

print(max(dp))

        