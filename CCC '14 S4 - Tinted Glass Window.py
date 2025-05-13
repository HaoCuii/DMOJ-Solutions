#coord compression + 2d diff array
n = int(input())
t = int(input())
glass = []
for i in range(n):
    a,b,c,d,e = map(int,input().split())
    glass.append((a,b,c,d,e))

x1, y1 = [], []
for a, b, c, d, e in glass:
    x1 += [a, c]
    y1 += [b, d]
xn = sorted(set(x1))
yn = sorted(set(y1))
x,y = {},{}
for i in range(len(xn)):
    x[xn[i]] = i
for i in range(len(yn)):
    y[yn[i]] = i

diff = [[0] * (len(xn)+1) for _ in range(len(yn)+1)]
for x1, y1, x2, y2, v in glass:
    x1, y1, x2, y2 = x[x1], y[y1], x[x2], y[y2]
    diff[y1][x1] += v
    diff[y1][x2] -= v
    diff[y2][x1] -= v
    diff[y2][x2] += v
for i in range(len(y)):
    for j in range(len(x)):
        if i > 0:
            diff[i][j] += diff[i - 1][j]
        if j > 0:
            diff[i][j] += diff[i][j - 1]
        if i > 0 and j > 0:
            diff[i][j] -= diff[i - 1][j - 1]

ans = 0
for i in range(len(yn)-1):
    for j in range(len(xn)-1):
        if diff[i][j] >= t:
            ans += (xn[j+1] - xn[j]) * (yn[i+1] - yn[i])

print(ans)

