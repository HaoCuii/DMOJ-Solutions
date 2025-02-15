N,M,A,B = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()

def dfs(node):
    if node == B:
        return True
    visited.add(node)
    for i in graph[node]:
        if i not in visited:
            if dfs(i):
                return True
    return False


if dfs(A):
    print('GO SHAHIR!')
else:
    print("NO SHAHIR!")

