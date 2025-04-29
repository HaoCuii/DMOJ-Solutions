n = int(input())
lim = 10**7 
sieve = [True] * (lim + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(lim**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, lim + 1, i):
            sieve[j] = False
sieve = [x for x, prime in enumerate(sieve) if prime]

for _ in range(n):
    c = int(input())
    fact = {}

    for p in sieve:
        if p * p > c:
            break
        while c % p == 0:
            fact[p] = fact.get(p, 0) + 1
            c //= p
    if c > 1:
        fact[c] = fact.get(c, 0) + 1
    
    ans = 1
    for i in fact:
        ans *= fact[i]*2 + 1
    print(ans)
    
    
