import copy
connections = []
adjacency_list = {}
bombings = []
while True:
    x = str(input())
    if x != '**':
        connections.append(x)
    else:
        break
for i in connections:
    z,y = ([*i])[0],([*i])[1]
    if z not in adjacency_list:
        adjacency_list[z] = []
        adjacency_list[z].append(y)
    if y not in adjacency_list:
        adjacency_list[y] = []
        adjacency_list[y].append(z)
    if y not in adjacency_list[z]:
        adjacency_list[z].append(y)
    if z not in adjacency_list[y]:
        adjacency_list[y].append(z)
def dfs(visited, adjacency_list, node):
    if node not in visited:
        if node == 'B':
            return True
        else:
            visited.append(node)
            for j in adjacency_list[node]:
                if dfs(visited.copy(),adjacency_list,j):
                    return True
    return False
for k in adjacency_list:
    for l in adjacency_list[k]:
        visited = []
        copy_adj = copy.deepcopy(adjacency_list)
        copy_adj[k].remove(l)
        if not dfs(visited,copy_adj,'A'):
            bombings.append(k)
            bombings.append(l)
counter = 0
for m in range(int(len(bombings)/2)):
    print(''.join(bombings[m+counter])+''.join(bombings[m+counter+1])),
    counter += 1
print('There are',(int(len(bombings)/2)),'disconnecting roads.')