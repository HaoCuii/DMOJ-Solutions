import math

c = int(input())
n = c**2+1
ans = float('inf')
for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
        a = i + c
        b = n//i + c
        ans = min(a+b,ans)

print(ans)