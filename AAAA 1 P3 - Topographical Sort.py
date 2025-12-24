import sys
t = int(input())    
n = int(input())

if t == 1:
    h = list(map(int,input().split()))
    pos = [[] for _ in range(n+1)]
    for i in range(n):
        pos[h[i]].append(i)

    active = [False] * n
    islands = 0
    ans = []

    for i in range(n,0,-1):
        for j in pos[i]:
            active[j] = True
            if (j == 0 or not active[j-1]) and (j == n-1 or not active[j+1]):
                islands += 1
            elif (j > 0 and active[j - 1]) and (j < n-1 and active[j+1]):
                islands -= 1
        ans.append(islands)
    print(*reversed(ans))

else: 
    c = list(map(int,input().split()))
    ans = [0] * n 
    island = 0 
    gap = 0 
    prev = 0
    
    for s in range(n,0,-1):
        target = c[s-1]
        diff = target - prev

        if diff > 0: #more islands
            for i in range(diff):
                if island*2 >= n:
                    print(-1)
                    sys.exit()
                
                ans[island*2] = s
                island += 1
                
        elif diff < 0: #less islands
            for i in range(-diff):
                if gap*2 + 1 >= n:
                    print(-1)
                    sys.exit()
                if island <= gap+1:
                    print(-1)
                    sys.exit()
                ans[gap*2+1] = s
                gap += 1
        
        prev = target

    print(*ans)