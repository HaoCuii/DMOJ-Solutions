import math
t = int(input())
def sum_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

for _ in range(t):
    a, b = map(int, input().split())
    hi = math.isqrt(a + b)
    sqrt_a = math.isqrt(a)
    sqrt_b = math.isqrt(b)

    split1 = min(sqrt_a, sqrt_b)
    sum1 = sum_squares(split1)
    sum1 += split1

    if sqrt_a > sqrt_b:
        sum2 = (sqrt_a - sqrt_b) * (b + 1)
    else:
        sum2 = 0
    if sqrt_b > sqrt_a:
        sum3 = (sqrt_b - sqrt_a) * (a + 1)
    else:
        sum3 = 0
    split4 = max(sqrt_a, sqrt_b)
    if hi > split4:
        sum4 = (hi - split4) * (a + b + 1)
        sum4 -= (sum_squares(hi) - sum_squares(split4))
    else:
        sum4 = 0
  
    total = sum1 + sum2 + sum3 + sum4
    print((total + 1) % 998244353)
