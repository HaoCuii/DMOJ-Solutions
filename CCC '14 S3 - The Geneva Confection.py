import sys
t = int(input())
for i in range(t):
    n = int(input())
    top = []
    for i in range(n):
        top.append(int(input()))
    branch = [float('inf')]
    end = [0]
    while True:
        if len(end) == n+1:
            print('Y')
            break
        if branch[-1] == end[-1] + 1:
            end.append(branch.pop())
        elif len(top) != 0 and top[-1] == end[-1] + 1:
            end.append(top.pop())
        elif len(top) != 0:
            branch.append(top.pop())  
        else:
            print('N')
            break


