import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
pwr = {} 

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(m):
        pwr[l[j]] = (i + 1, j + 1)

for i in range(q):
    k, r1, c1, r2, c2 = map(int, input().split())
    try:
        row, col = pwr[k]
        if r1 <= row <= r2 and c1 <= col <= c2:
            print('yes')
        else:
            print('no')
    except KeyError:
        print('no')
