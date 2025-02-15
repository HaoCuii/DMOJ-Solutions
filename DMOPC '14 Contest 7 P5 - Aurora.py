N,M = map(int,input().split())
A,B,C = map(int,input().split())
soldiers = list(map(int,input().split()))

sorted_soldiers = sorted(soldiers)
psa_aurora = [0]
for i in range(1,N+1):
    psa_aurora.append((sorted_soldiers[i-1]-1)*A + psa_aurora[i-1])

psa_para = [0]
for i in range(1,N+1):
    psa_para.append((sorted_soldiers[i-1]-1)*B + psa_para[i-1])

shortest_time = float('inf')
stop_time = 0

for i in range(N+1):
    aurora = psa_aurora[-1] - psa_aurora[i] + max(0,(((N-1-i)*(N-i))/2)*C)
    para = psa_para[i]
    shortest_time = min(shortest_time, aurora+para)

    
print(int(shortest_time))
    