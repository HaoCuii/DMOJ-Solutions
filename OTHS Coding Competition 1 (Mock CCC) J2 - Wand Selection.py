n = int(input())
big = 0
total = 0
for i in range(n):
    x = int(input())
    total += x
    big = max(big,x)

print(int((total-big)/n))