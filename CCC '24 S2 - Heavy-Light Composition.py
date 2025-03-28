import math
import sys

n, m, r, c = list(map(int, input().split()))
poster = []

for i in range(n):
    row = []
    for j in range(m):
        row.append('b')
    poster.append(row)

if r == 0 and c == 0:
    for i in range(m):
        poster[0][i] = 'a'
    for i in range(n):
        poster[i][0] = 'c'
    poster[0][0] = 'b'
elif r == n:
    if m % 2 == 0 and c % 2 == 1:
        print('IMPOSSIBLE')
        sys.exit()
    for i in range(m):
        poster[0][i] = 'a'

    left, right = m // 2, m // 2
    if c % 2 == 0:
        left -= 1
        if  m % 2 != 0:
            right += 1
    for i in range(math.ceil(c / 2)):
        for j in range(r):
            poster[j][left] = 'a'
            poster[j][right] = 'a'
        left -= 1
        right += 1

elif c == m:
    if n % 2 == 0 and r % 2 == 1:
        print('IMPOSSIBLE')
        sys.exit()
    for i in range(n):
        poster[i][0] = 'a'

    top, bottom = n // 2, n // 2
    if r % 2 == 0:
        top -= 1
        if n %  2 != 0:
            bottom += 1
    for i in range(math.ceil(r / 2)):
        for j in range(c):
            poster[top][j] = 'a'
            poster[bottom][j] = 'a'
        top -= 1
        bottom += 1

else:
    if r  == 0:
        for i in range(m-1,c-1,-1):
            poster[-1][i] = 'c'
    elif c == 0:
        for i in range(n-1,r-1,-1):
            poster[i][-1] = 'c'
        
    for i in range(r):
        for j in range(m):
            poster[i][j] = 'a'
    for i in range(c):
        for j in range(n):
            poster[j][i] = 'a'
for i in poster:
    print(''.join(i))