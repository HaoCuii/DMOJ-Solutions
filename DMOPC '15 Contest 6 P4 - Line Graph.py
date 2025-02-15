n,k = map(int,input().split())

weights = list(map(float,input().split()))
for i in range(n-1):
    weights[i] = (weights[i],i,i+1)

for i in range(max(0,n-k)):
    weights.append((0,i,i+k))

sorted_weights = sorted(weights)

Parent = [i for i in range(n)]
Rank = [0] * n

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

mst = 0
for (c,a,b) in sorted_weights:

    if find(a) != find(b):
        mst += c
        union(a,b)

print(int(mst))
