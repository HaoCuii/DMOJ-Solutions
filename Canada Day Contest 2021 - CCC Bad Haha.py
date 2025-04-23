import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = list(map(int, input().strip()))
    k = int(input())
    end = []
    j = 0

    while k > 0 and j < len(n)-1:
        if n[j] > n[j+1]:
            end.append(n[j])
            k -= 1
            n.pop(j)
            j = max(0,j-1)
        else:
            j += 1
    
    if end != []:
        smallest = sorted(end)[0]
        while k > 0:
            if n[-1] > smallest:
                end.append(n.pop())
                k -= 1
            else:
                break  
    n.extend(sorted(end))
    print(''.join(list(map(str,n))))