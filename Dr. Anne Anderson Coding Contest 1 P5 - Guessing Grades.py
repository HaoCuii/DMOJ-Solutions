n = int(input())
wil = list(input())
kev = list(input())
a,b,c,d = map(int,input().split())
count = {'A':a,'B':b,'C':c,'D':d}
total = 0
new = []
for i in range(n):
    if kev[i] != '?':
        count[kev[i]] -= 1
        if wil[i] == kev[i]:
            total += 1
    else:
        new.append(wil[i])
A,B,C,D = new.count('A'),new.count('B'),new.count('C'),new.count('D')
largest = sorted(count.items(),key=lambda item: item[1],reverse=True)

for i in range(4):
    ans,cnt = largest[i]
    for j in range(i+1,4):
        ans2,cnt2 = largest[j]
        temp = globals()[ans2] - min(globals()[ans2],cnt)
        if globals()[ans2] > cnt:
            cnt = 0
            break
        else:
            cnt -= globals()[ans2]
        globals()[ans2] = temp

    for j in range(i):
        ans2,cnt2 = largest[j]
        temp = globals()[ans2] - min(globals()[ans2],cnt)
        if globals()[ans2] > cnt:
            globals()[ans2] -= cnt
            cnt = 0
            break
        else:
            cnt -= globals()[ans2]
        globals()[ans2] = temp
    if cnt > 0:
        total += cnt
        globals()[ans] -= cnt
        
print(total)

