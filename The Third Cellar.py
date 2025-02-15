n = int(input())
upper = 0
inputs = []
for i in range(n):
    l,u = map(int,input().split())
    if u > upper:
        upper = u
    inputs.append((l,u))

prime = [True for _ in range(upper+1)]
# boolean array
p = 2
while (p * p <= upper):
    if (prime[p] == True):
        for i in range(p * p, upper+1, p):
            prime[i] = False
    p += 1

for (a,b) in inputs:
    total = 0
    for i in range(max(2,a), b):
        if prime[i]:
            total += 1

    print(total)
