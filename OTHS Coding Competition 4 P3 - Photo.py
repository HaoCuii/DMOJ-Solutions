MOD = 10**9

n, q = map(int, input().split())
pot = list(map(int, input().split()))
table = [0] * (n + 1)

if pot[0] == 0:
    for i in range(1, n + 1):
        table[i] = pot[i - 1] % MOD
    first = 1
else:
    for i in range(1, n + 1):
        table[i] = pot[i - 1]  
    first = pot[0]
table[1] = 1

for _ in range(q):
    cmd = list(map(int, input().split()))
    t = cmd[0]
    
    if t == 3:
        pos = cmd[1]
        ans = (table[pos] * first) % MOD
        print(int(ans))
        
    elif t == 2:
        first = (first * cmd[1]) % MOD
        
    else:
        pos, v = cmd[1], cmd[2]
        if first == 0:
            table[pos] = (table[pos] + v)
        else:
            table[pos] = (table[pos] * first + v) // first
