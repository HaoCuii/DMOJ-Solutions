#dp[i][j][k][l][m][n] i is amount of 1's, j is amount of 2's and so on. 
#Represents whether that position is winning or losing
import heapq
dp = [[[[[["L" for _ in range(5)] for _ in range(5)] for _ in range(5)]
        for _ in range(5)] for _ in range(5)] for _ in range(5)]
pq = []
visited = set()

heapq.heappush(pq, (0, 0, 0, 0, 0, 0, 0))

while pq:
    cnt, i, j, k, l, m, n = heapq.heappop(pq)
    played = 84-cnt
    key = (i, j, k, l, m, n)
    if key in visited:
        continue
    visited.add(key)

    #Check Previous states to see whether this one is w/l
    win = False
    counts = [i, j, k, l, m, n]
    for idx in range(6):
        if counts[idx] > 0: 
            counts[idx] -= 1
            new_sum_played = 84-cnt + (idx+1)
            if new_sum_played > 31:
                continue
            if dp[counts[0]][counts[1]][counts[2]][counts[3]][counts[4]][counts[5]] == "L":
                win = True
            counts[idx] += 1 

    if win and played <= 31:
         dp[i][j][k][l][m][n] = "W" 

    #Push future states into pq
    counts = [i, j, k, l, m, n]
    for idx in range(6):
        if counts[idx] < 4: 
            counts[idx] += 1
            heapq.heappush(pq,((counts[0]*1+counts[1]*2+counts[2]*3+counts[3]*4+counts[4]*5+counts[5]*6),
                                     counts[0],counts[1],counts[2],counts[3],counts[4],counts[5]))
            counts[idx] -= 1 

n =     int(input())
for _ in range(n):
    crd = list(input())
    curr_player = 'A' if len(crd) % 2 == 0 else 'B'
    id = [4,4,4,4,4,4]
    for element in crd:
        id[int(element)-1] -= 1
    if dp[id[0]][id[1]][id[2]][id[3]][id[4]][id[5]] == "W":
        print(curr_player)
    else:
        print('B' if curr_player == 'A' else 'A')