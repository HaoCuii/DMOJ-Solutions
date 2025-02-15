N,M = map(int,input().split())

Parent = [i for i in range(N+1)]
Rank = [0] * (N + 1)

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

for i in range(M):
    l = list(map(int,input().split()))
    for i in range(2,l[0]+1):
        if find(l[1]) != find(l[i]):
            union(l[1],l[i])

infected = []
for i,parent in enumerate(Parent):
    if find(parent) == find(Parent[1]):
        infected.append(str(i))

print(len(infected))
print(' '.join(infected))

