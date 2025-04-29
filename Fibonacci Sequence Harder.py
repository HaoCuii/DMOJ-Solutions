import sys

N = "00" + bin(int(sys.stdin.readline()))
MOD = 10**9 + 7

f0, f1 = 1, 0

for c in N:
    temp = f0
    f0 = (f0 * f0 + f1 * f1) % MOD
    f1 = (f1 * (2 * temp + f1)) % MOD

    if c == '1':
        temp = f0
        f0 = f1
        f1 = (f1 + temp) % MOD

print(f1)