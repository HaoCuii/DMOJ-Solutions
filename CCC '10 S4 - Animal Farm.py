x = int(input())
graph_inside = []
graph_outside = []
seen = [['a','b','c','d','e']]

for iteration in range(x):
    l = list(map(int,input().split()))
    p1, p2 = 1, 2
    for i in range(l[0]):
        if p1 == l[0]:
            p2 = 1
        a, b, c = l[p1], l[p2], l[p1 + l[0]]
        found = False
        for item in seen:
            if item[:2] == ([min(a, b), max(a, b)]):
                item.append(iteration + 1)
                graph_inside.append(item)
                found = True
                break
        if not found:
            seen.append([min(a, b), max(a, b), c, iteration + 1])
        p1 += 1
        p2 += 1

for i in seen:
    if i == ['a', 'b', 'c', 'd', 'e']:
        pass
    else:
        if len(i) == 4:
            i.append(0)
        graph_outside.append(i)

distinct_in = 0


for i in range(len(graph_inside)):
    graph_inside[i] = graph_inside[i][2:]
    if graph_inside[i][1] > distinct_in:
        distinct_in = graph_inside[i][1]
    if graph_inside[i][2] > distinct_in:
        distinct_in = (graph_inside[i][2])

for i in range(len(graph_outside)):
    graph_outside[i] = graph_outside[i][2:]

distinct_out = distinct_in + 1

Parent = [i for i in range(distinct_in+1)]
Rank = [0] * (distinct_in + 1)
graph_inside = sorted(graph_inside)
graph_outside = sorted(graph_outside)

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

total_inside = 0
distinct_edges = 0

for (c,a,b) in graph_inside:
    if find(a) != find(b):
        distinct_edges += 1
        total_inside += c
        union(a,b)

if distinct_edges < distinct_in - 1:
    total_inside = float('inf')

Parent = [i for i in range(distinct_out+1)]
Rank = [0] * (distinct_out + 1)
total_outside = 0
for (c,a,b) in graph_outside:
    if find(a) != find(b):
        total_outside += c
        union(a,b)
print(min(total_outside,total_inside))
