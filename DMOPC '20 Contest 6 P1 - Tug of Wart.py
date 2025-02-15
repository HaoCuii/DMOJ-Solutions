from collections import deque
import sys
n = int(input())
l = deque(map(int, sys.stdin.readline().split()))
l_clone = deque(l)


psa = deque([0] * n)
psa[0] = l[0]
for i in range(1, n):
    psa[i] = psa[i - 1] + l[i]

def binarysearch(arr, target, low, high, const):
    while low <= high:
        midpoint = (low + high) // 2
        adjusted_mid = arr[midpoint] - const

        if adjusted_mid == target:
            return midpoint, midpoint
        elif adjusted_mid < target:
            low = midpoint + 1
        else:
            high = midpoint - 1

    if low >= len(arr):
        return high, high
    if high < 0:
        return low, low
    
    adjusted_low = arr[low] - const
    adjusted_high = arr[high] - const

    if abs(adjusted_low - target) < abs(adjusted_high - target):
        return low, low
    elif abs(adjusted_high - target) < abs(adjusted_low - target):
        return high, high
    else:
        return low, high

avg = psa[n-1] // 2
total = psa[n-1]
out = []
neg = 0

for i in range(n):
    a, b = binarysearch(psa, avg, 0, n - 1,neg)
    dif1 = abs(total - (2 * (psa[a]-neg)))
    dif2 = abs(total - (2 * (psa[b]-neg)))
    out.append(str(min(dif1, dif2)))
    neg += l_clone[i]

    l.append(l.popleft())
    psa.popleft()
    psa.append(psa[-1]+l_clone[i])


print(' '.join(out))
