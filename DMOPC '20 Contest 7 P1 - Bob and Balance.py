n = int(input())
l = list(map(int,input().split()))

for i in range(n*2):
    l[i] = ((l[i],i+1))


l = sorted(l)
l1,l2 = l[0:n],l[n:n*2]

tip = 0
tips = []

for i in range(n):
    tips.append((l1[i][1],l2[i][1]))
    if l1[i][0] < l2[i][0]:
        tip += 1

print(tip)

for (a,b) in tips:
    print(a,b)
    