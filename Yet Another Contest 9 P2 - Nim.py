import sys

t = int(input())
input = sys.stdin.readline
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    stones = [0,0]

    for i in range(len(l)):
        if l[i] == 1:
            stones[0] += 1
        else:
            stones[1] += 1
    
    if stones[1] == 0:
        if stones[0] % 2 == 0:
            print("Mike")
        else:
            print("Josh")

    elif stones[0] == 0:
        print("Mike")
    
    else:
        if stones[0] % 2 == 0:
            print("Mike")
        else:
            print("Josh")