import sys

n = int(input())

lo = 1
hi = 44721 

while lo <= hi:
    mid = (lo + hi) // 2
    current_sum = mid * (mid + 1) // 2 
    if current_sum == n:
        a = mid * (mid + 1) // 2
        b = (mid - 1) * mid // 2
        result = a * (a + 1) // 2 - b * (b + 1) // 2
        print(result)
        sys.exit()
    elif current_sum < n:
        lo = mid + 1
    else:
        hi = mid - 1

a = lo * (lo + 1) // 2
b = hi * (hi + 1) // 2
result = a * (a + 1) // 2 - b * (b + 1) // 2
print(result)
