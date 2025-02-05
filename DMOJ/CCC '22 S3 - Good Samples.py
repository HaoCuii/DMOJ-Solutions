n,m,k = map(int,input().split())

total_substrings = (n*2 + n) / 2
best_sample = []

for i in range(n):
    best_sample.append(i%m + 1)

print(best_sample)

