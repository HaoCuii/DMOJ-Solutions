import sys

N,M,K = map(int,sys.stdin.readline().split())
blocks = []

for i in range(K):
    blocks.append(list(map(int,(sys.stdin.readline().split()))))

blocks.sort(reverse=True)

col = -1
total = 0
under = 0

for i in blocks:
    if i[0] != col:
        col = i[0]
        total += i[1]
    else:
        under += 1

print(total-under)




