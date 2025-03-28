n = int(input())
ppl = []
for i in range(n):
    ppl.append(int(input()))

match = 0
for i in range(n//2):
    if ppl[i] == ppl[i+n//2]:
        match += 2

print(match)
