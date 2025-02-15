N = int(input())
house = []
for i in range(N):
    house.append(float(input()))
house = sorted(house)
hyd = int(input())

def valid(hoselength):
    hydrants = hyd
    houses = N
    connected = [False] * N
    for i in range(N):
        if connected[i]:
            continue
        connected[i] = True
        hydrants -= 1
        houses -= 1
        for j in range(i+1,len(house)):
            if not connected[j] and min(house[j] - house[i], 1000000 - (house[j]- house[i])) <= hoselength*2:
                connected[j] = True
                houses -= 1
    if houses >= 0 and hydrants >= 0:
        return True
    else:
        return False

left = 0
right = 1000000
while left < right:
    mid = (left + right) // 2  
    if valid(mid):
        right = mid
    else:
        left = mid + 1

print(right)
    


