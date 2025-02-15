n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


pos = [0] * (n + 1) 

for i in range(n):
    value = y[i]
    pos[value] = i


cuts = 1
last_position = pos[x[0]]

for i in range(1, n):
    current_position = pos[x[i]]
    if current_position != last_position + 1:
        cuts += 1
    last_position = current_position 

print(cuts)