#why does this code work???? I have no clue why lol.

n = int(input())
friends = []  # p,w,d
for i in range(n):
    p, w, d = map(int, input().split())
    w = 1/w
    friends.append([p, w, d])
friends.sort()

newfriends = [] #p,w,d,(l or r)
for i in range(n):
    p,w,d = friends[i]
    newfriends.append([p-d,w,d,"l"])
    newfriends.append([p+d,w,d,"r"])
newfriends.sort()


# equation sort of equals x(m1 + m2 + m3... ) + b1 + b2 + b3... updated at every xi.
k = 0
while k < 2*n and newfriends[k][0] == newfriends[0][0]:
    k += 1

m = 0
b = 0

for i in range(k, 2*n):
    if newfriends[i][3] == "l":
        m += -(1 / newfriends[i][1])
        b += (newfriends[i][0]) / newfriends[i][1]

ans = newfriends[0][0]*m + b
idx = k

while (idx < n*2):
    k = 0
    while idx+k < n*2 and newfriends[idx+k][0] == newfriends[idx][0]:
        k += 1
    for i in range(k):
        if newfriends[idx+i][3] == "l":
            m += (1 / newfriends[idx+i][1])
            b += -(newfriends[idx+i][0] / newfriends[idx+i][1])
        else:
            m += 1 / newfriends[idx+i][1]
            b += -(newfriends[idx][0] / newfriends[idx+i][1])
    ans = min(ans,newfriends[idx][0] * m + b)
    idx += k


print(round(ans))


    


