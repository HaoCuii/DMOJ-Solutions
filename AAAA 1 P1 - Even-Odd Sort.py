n = int(input())
nums = list(map(int,input().split()))

odd = 0
even = 0
for i in nums:
    if i % 2 != 0:
        odd += 1

if n % 2 != 0:
    print("Steven")
else:
    if odd > n // 2:
        print("Todd")
    else:
        print("Steven")