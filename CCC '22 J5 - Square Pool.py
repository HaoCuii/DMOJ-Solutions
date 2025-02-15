n = int(input())
t = int(input())

trees_r = []
trees_c = []

for i in range(t):
    r,c = map(int,input().split())
    trees_r.append((r,c))
    trees_c.append((c,r))

trees_r,trees_c = sorted(trees_r),sorted(trees_c)

trees_r.append(0)
trees_c.append(n+1)




 

