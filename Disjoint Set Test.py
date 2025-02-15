import sys
input = sys.stdin.readline
n,m = map(int,input().split())
sorted_edges = []
for i in range(m):
    a,b = map(int,input().split())
    sorted_edges.append((a,b))

Parent = [i for i in range(n+1)]
Rank = [0] * (n + 1)

def find(x):
    if Parent[x] != x:
        return find(Parent[x])
    else:
        return x

def union(x,y):
    x_root, y_root =  find(y), find(x)
    if Rank[x_root] < Rank[y_root]:
        Parent[x_root] = y_root
    elif Rank[x_root] > Rank[y_root]:
        Parent[y_root] = x_root
    else:
        Parent[y_root] = x_root
        Rank[x_root] += 1

mst = []
for (a,b) in sorted_edges:
    if find(a) != find(b):
        mst.append((a,b))
        union(a,b)

if len(mst) != n - 1:
    print("Disconnected Graph")
else:
    for i in mst:
        print(i)