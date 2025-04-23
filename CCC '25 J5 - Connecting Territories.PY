r, c, m = int(input()), int(input()), int(input())

cur = [0 for _ in range(c)]

for i in range(c):
    cur[i] = ((r - 1) * c + i) % m + 1

for i in range(1, r):
    next = [float("inf")] * c  
    for j in range(c):
        cost = ((r - i - 1) * c + j) % m + 1
        next[j] = cost + cur[j]
        if j > 0:
            next[j] = min(next[j], cost + cur[j - 1])
        if j < c - 1:
            next[j] = min(next[j], cost + cur[j + 1])
    cur = next 

print(min(cur)) 
