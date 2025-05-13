import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

bad = []
for i in range(1, n-1):
    if not ((a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1])):
        bad.append(i)

if not bad:
    print(0)
    sys.exit()
if len(bad) > 3:
    print(-1)
    sys.exit()

cand = set(range(max(0, bad[0]-1), min(n, bad[0]+2)))
for i in bad[1:]:
    cand &= set(range(max(0, i-1), min(n, i+2)))

for i in cand:
    orig = a[i]
    for d in (-1, 1):
        a[i] = orig + d
        ok = True
        for j in range(max(1, i-1), min(n-1, i+2)):
            if not ((a[j] > a[j-1] and a[j] > a[j+1]) or (a[j] < a[j-1] and a[j] < a[j+1])):
                ok = False
                break
        if ok:
            print(1)
            sys.exit()
    a[i] = orig

print(-1)
