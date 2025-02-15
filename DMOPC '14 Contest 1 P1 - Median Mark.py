import math
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
s = sorted(l)
if n % 2 == 0:
    if (s[n//2]+s[n//2-1])/2 * 2 % 1 == 0:
        print(math.ceil((s[n//2]+s[n//2-1])/2))
    else:
        print(round((s[n//2]+s[n//2-1])/2))
else:
    print(s[n//2])
