from collections import deque

n = int(input())
nagato = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    nagato[a].append(b)
    nagato[b].append(a)

depth = [[0, 0] for _ in range(n + 1)]
order = []
stack = [(1, -1)] 

while stack:
    node, parent = stack.pop()
    order.append((node, parent))
    for neighbor in nagato[node]:
        if neighbor != parent:
            stack.append((neighbor, node))

for node, parent in reversed(order):
    max_depth1, max_depth2 = 0, 0
    for neighbor in nagato[node]:
        if neighbor == parent:
            continue
        child_depth = depth[neighbor][0] + 1
        if child_depth > max_depth1:
            max_depth2 = max_depth1
            max_depth1 = child_depth
        elif child_depth > max_depth2:
            max_depth2 = child_depth
    depth[node] = [max_depth1, max_depth2]

queue = deque([(1, -1)])  

while queue:
    node, parent = queue.popleft()
    for neighbor in nagato[node]:
        if neighbor == parent:
            continue
        queue.append((neighbor, node))

        if depth[node][0] == depth[neighbor][0] + 1:
            parent_depth = depth[node][1] + 1  
        else:
            parent_depth = depth[node][0] + 1 

        if parent_depth > depth[neighbor][0]:
            depth[neighbor][1] = depth[neighbor][0]
            depth[neighbor][0] = parent_depth
        elif parent_depth > depth[neighbor][1]:
            depth[neighbor][1] = parent_depth

for i in range(1, n + 1):
    print(depth[i][0] + 1)
