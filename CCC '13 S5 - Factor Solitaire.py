n = int(input())
cost = 0

while n > 1:
    boolean = False
    f = 0
    for i in range(2,n//2+1):
        if n % i == 0:
            f = i
            boolean = True
            break

    if boolean:
        z = int(n/f)
        n -= z
        cost += n // z
    else:
        n -= 1
        cost += n

print(cost)
    