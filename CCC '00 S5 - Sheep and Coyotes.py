from decimal import *
from math import sqrt

getcontext().prec = 20
sheeps = []

for i in range(int(input())):
    x = Decimal(input())
    y = Decimal(input())
    sheeps.append((x,y))

print(sheeps)
wolf = Decimal(0)
edible_sheep = set()

for _ in range(100000):
    lowest = float('inf')
    sheep = []
    for (x,y) in sheeps:
        d_squared = x**2 + (y-wolf)**2
        d = Decimal(sqrt(d_squared))
        if d < lowest:
            lowest = d
            sheep = [(x,y)]
        elif d == lowest:
            sheep.append((x,y))
    for i in sheep:
        edible_sheep.add(i)
    wolf += Decimal(0.01)

print(list(edible_sheep))