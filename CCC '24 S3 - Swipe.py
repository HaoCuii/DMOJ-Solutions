'''
m/2 subtask, only works if the compressed b is a subset of a
'''
import sys
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

newb = [-1]
for i in b:
    if i != newb[-1]:
        newb.append(i)
newb = newb[1:]
idx = 0
for i in newb:
    while idx < n:
        if a[idx] == i:
            break
        idx += 1
    if idx == n:
        print('NO')
        sys.exit()
print('YES')
left = []
right =[]
l,r = 0,0
for i in range(n):
    boo = False
    while (r < n and a[i] == b[r]):
        r+= 1
        boo = True
    if boo:
        if r <= i:
            right.append(("L", l, i))
        elif l >= i:
            left.append(("R",i,r-1))
        else:
            right.append(("L", l, i))
            left.append(("R",i,r-1))
    l = r

print(len(left)+len(right))
for a,b,c in reversed(left):
    print(a,b,c)
for a,b,c in right:
    print(a,b,c)
