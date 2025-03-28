from collections import deque

n = int(input())

graph = {}
for i in range(1, n + 1):
    choices = list(map(int, input().split()))
    m = choices[0]
    if m > 0:
        graph[i] = choices[1:]
    else:
        graph[i] = []

visited = set()
queue = deque()
queue.append((1, 1)) 
visited.add(1)
shortest_path = float('inf')
all_reachable = True

while queue:
    current_page, path_length = queue.popleft()
    if not graph[current_page]:
        shortest_path = min(shortest_path, path_length)

    for next_page in graph[current_page]:
        if next_page not in visited:
            visited.add(next_page)
            queue.append((next_page, path_length + 1))


for page in range(1, n + 1):
    if page not in visited:
        all_reachable = False
        break

if all_reachable:
    print("Y")
else:
    print("N")
print(shortest_path)



'''
import sys

dusa_size = int(sys.stdin.readline().strip())
    
for line in sys.stdin:
    yobi_size = int(line.strip())
        
    if yobi_size < dusa_size:
        dusa_size += yobi_size  # Absorb the Yobi's size
    else:
        print(dusa_size)  # Output the size when Dusa runs away
