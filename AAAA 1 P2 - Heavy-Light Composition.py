lights,friends = map(int,input().split())
l = list(map(int,input().split()))
f = list(map(int,input().split()))

idx = 0
ans = 0


l.sort()
f.sort()

#handle edge cases
if f[0] < l[0]:
    ans += (l[0] - f[0])
    while idx < friends and f[idx] < l[0]:
        idx += 1
if f[-1] > l[-1]:
    ans += (f[-1] - l[-1])

for i in range(len(l) - 1):
    left = l[i]
    right = l[i+1]
    prev = left 
    max_gap = 0
    
    while idx < friends and f[idx] < right:
        current = f[idx]
        gap = current - prev
        if gap > max_gap:
            max_gap = gap
        prev = current
        idx += 1
        
    final_gap = right - prev
    if final_gap > max_gap:
        max_gap = final_gap

    ans += (right - left) - max_gap

print(ans)