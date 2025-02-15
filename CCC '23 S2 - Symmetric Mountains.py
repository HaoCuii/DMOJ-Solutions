import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
cr = [float('inf')] * n

#odd
for i in range(n):
    t = 0
    l = i
    h = i
    for j in range(n):
        t += abs(m[l] - m[h])
        cr[j*2] = min(cr[j*2],t)
        if l - 1 >= 0 and h + 1 < n:
            l -= 1
            h += 1
        else:
            break

#even
for i in range(n):
    t = 0
    l = i
    if i+1 < n:
        h = i+1
    else:
        break
    for j in range(n):
        t += abs(m[l] - m[h])
        cr[j*2+1] = min(cr[j*2+1],t)
        if l - 1 >= 0 and h + 1 < n:
            l -= 1
            h += 1
        else:
            break
print(' '.join(list(map(str,cr))))