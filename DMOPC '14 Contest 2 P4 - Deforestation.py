N = int(input())
psa = [0]

for i in range(1,N+1):
    x = int(input())
    psa.append(x + psa[i-1])

Q = int(input())

for i in range(Q):
    a,b = map(int,input().split())
    print(psa[b+1]-psa[a])