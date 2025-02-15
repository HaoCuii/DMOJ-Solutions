N,L,S = map(int,input().split())
houses = {}
counter = 0

for _ in range(N):
    a, b, s = map(int, input().split())
    houses[a] = houses.get(a, 0) + s
    houses[b+1] = houses.get(b+1, 0) - s

sorted_houses = sorted(houses)
spooky = 0
for i in sorted_houses:
    if spooky > 0:
        L -= (i-spooky)
        spooky = 0
    counter += houses[i]
    if counter >= S:
        spooky = i

print(L)





