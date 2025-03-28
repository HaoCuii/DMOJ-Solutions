n = int(input())
a = int(input())
b = int(input())

if a > b:
    print("NO")
elif (b-a) % 2 == 0:
    print("YES")
else:
    print("NO")
