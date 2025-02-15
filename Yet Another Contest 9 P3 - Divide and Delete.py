import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
goods = 0 

def gf(n):
    largestPrime = 1
    while n % 2 == 0:
        largestPrime = 2
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            largestPrime = i
            n //= i
        i += 2
    if n > 2:
        largestPrime = n

    return largestPrime

gf_list = []
for i in arr:
    gf_list.append(gf(i))

blocks = []

for i in range(n,0,-1):
    if gf_list[i-1] > 1:
        blocks.append(i)
    for j in range(1,len(blocks)+1):
        if gf_list[blocks[-1]-1] <= blocks[-1] - i + 1:
            blocks.pop()
        else:
            break
    
    if len(blocks) > 0:
        goods += (blocks[-1]-i)
    else:
        goods += n-i+1

print(goods)
    
    