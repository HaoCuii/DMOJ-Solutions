import sys
n,m = map(int,input().split())
for i in range(n):
    l,r = [],[]
    for j in range(1,m+1):
        l.append(j+(2*m*i))
        r.append((j+m)+(2*m*i))
    r = list(reversed(r))
    
    for j in range(2*m):
        s = int(input())
        if len(l) > 0 and l[-1] == s:
            l.pop()
        elif len(r) > 0 and r[-1] == s:
            r.pop()
        else:
            print('no')
            sys.exit()
print('yes')
    