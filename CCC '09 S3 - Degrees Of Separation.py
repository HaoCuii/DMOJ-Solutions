from collections import deque
visited = set()
graph ={
    1: [6], 2: [6], 3: [4, 5, 6, 15], 4: [3, 5, 6], 5: [3, 4, 6], 6: [1, 2, 3, 4, 5, 7], 7: [6, 8],
    8: [7, 9], 9: [8, 10, 12], 10:[9, 11], 11:[10, 12], 12:[9, 11, 13], 13:[12, 14, 15], 14:[13], 
    15:[3,13], 16:[17,18], 17:[16,18], 18:[16,17],
}

def shortest_path(adj_list, start, end):
    queue = deque([(start, 0)])
    visited = set([start]) 
    while queue:
        node, path_len = queue.popleft()
        if node == end:
            return path_len    
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path_len + 1)) 
    return None

def i(adj_list,x,y):
    try:
        adj_list[x].append(y)
    except KeyError:
        adj_list[x] = [y]
    try:
        adj_list[y].append(x)
    except KeyError:
        adj_list[y] = [x]

def d(adj_list,x,y):
    adj_list[x].remove(y)
    adj_list[y].remove(x)

def n(adj_list,x):
    return len(adj_list[x])

def f(adj_list,x):
    friend_of_friends = 0
    seen_friends = [x]
    for i in adj_list[x]:
        seen_friends.append(i)
    for i in adj_list[x]:
        for j in adj_list[i]:
            if j not in seen_friends:
                seen_friends.append(j)
                friend_of_friends += 1
    return friend_of_friends

while True:
    m = input()
    if str(m) == 'q':
        break
    if str(m) == 'i':
        x,y = int(input()),int(input())
        i(graph,x,y)
    elif str(m) == 'd':
        x,y = int(input()),int(input())
        d(graph,x,y)
    elif str(m) == 'n':
        x = int(input())
        print(n(graph,x))
    elif str(m) == 'f':
        x = int(input())
        print(f(graph,x))
    elif str(m) == 's':
        x,y = int(input()),int(input())
        sp = shortest_path(graph, x,y)
        if sp:
            print(sp)
        else:
            print("Not connected")

    

