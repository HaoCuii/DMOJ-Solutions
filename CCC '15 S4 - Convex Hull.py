import heapq
import sys

hull, num_islands, sea_routes = map(int, sys.stdin.readline().split())
dist = [[float('inf')]*hull for _ in range(num_islands + 1)]


graph = [[] for _ in range(num_islands+1)]


for _ in range(sea_routes):
    isl1, isl2, time,hull_cost = map(int,sys.stdin.readline().split())
    graph[isl1].append([isl2,time,hull_cost])
    graph[isl2].append([isl1,time,hull_cost])

start,end = map(int,sys.stdin.readline().split())
queue = [(0,0,start)]

while queue:
    t,h,isl = heapq.heappop(queue)
    for i in graph[isl]:
        nh,nt = i[2] + h, i[1] + t
        if nh < hull and nt < dist[i[0]][nh]: 
            dist[i[0]][nh] = nt
            heapq.heappush(queue,(nt,nh,i[0]))

if min(dist[end]) == float('inf'):
    print(-1)
else:
    print(min(dist[end]))