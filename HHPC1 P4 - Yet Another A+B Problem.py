import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    c = int(input())
    fact = {}

    p = 2
    while p * p <= c:
        while c % p == 0:
            fact[p] = fact.get(p, 0) + 1
            c //= p
        p += 1
    
    if c > 1:  
        fact[c] = fact.get(c, 0) + 1
    ans = 1
    for prime in fact:
        ans *= fact[prime] * 2 + 1
    
    print(ans)
