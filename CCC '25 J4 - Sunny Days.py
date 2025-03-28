n = int(input())
arr = [input() for _ in range(n)]

l = 0
rain = 0
ans = 0
skibidi = False

for i in range(n):
    if arr[i] == "P":
        rain += 1
        skibidi = True
    while rain > 1:
        if arr[l] == "P":
            rain -= 1
        l += 1
    ans = max(ans, i - l + 1)

if not skibidi:
    ans -= 1

print(ans)