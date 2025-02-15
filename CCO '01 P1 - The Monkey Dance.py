from math import lcm


def dfs(node, vis):
    global length
    length += 1
    vis.add(node)
    for i in graph[node]:
        if i not in vis:
            dfs(i, vis)

while True:
    n = int(input())
    if n == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        a,b = map(int,input().split())
        graph[a].append(b)

    vis = set()
    c = []
    for i in range(n):
        if i not in vis:
            length = 0
            dfs(i,vis)
            c.append(length)
    result = 1
    for i in c:
        result = lcm(result, i)

    print(result)