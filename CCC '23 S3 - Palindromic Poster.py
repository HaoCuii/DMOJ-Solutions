import math
n,m,r,c = list(map(int,input().split()))

poster = []
if n != 2:
    for i in range(n):
        row = []
        for j in range(m):
            if i != n-1:
                row.append('a')
            else:
                row.append('b')
        row[0] = 'b'
        if i == 0:
            row[-1] = 'b'
        if i == n-1:
            row[-1] = 'a'
            
        poster.append(row)
else:
    if (m % 2 == 0 and c % 2 == 1) or (c >= math.ceil(m/2)+1 and r <= 1):
        print(math.ceil(n/2)-1)
        print(-1)
        exit()
    else:
        for i in range(n):
            row = []
            for j in range(m):
                if i == 0:
                    row.append('a')
                else:
                    row.append('b')
            poster.append(row)
        if r == 0 or r == 1:
            poster[0][0] = 'b'
        if r == 0 or r == 2:
            poster[1][0] = 'a'

        l,r = m//2,m//2
        if c % 2 == 0:
            l -= 1
            r += 1
        for i in range(math.ceil(c/2)):
            poster[1][l] = 'a'
            poster[1][r] = 'a'
            l += 1; r -= 1

for i in poster:
    print(''.join(i))
    