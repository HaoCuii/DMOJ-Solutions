import math
while True:
    r = int(input())
    if r == 0:
        break
    total = 0
    for i in range(r+1):
        total += int(math.sqrt(r**2 - i**2))
    print(total*4 +1)
        