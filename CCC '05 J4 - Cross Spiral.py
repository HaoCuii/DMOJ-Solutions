length, width, length2, width2, steps = int(input()),int(input()),int(input()),int(input()),int(input())
graph = []

#Setting up graph
def cutout(a):
    for k in range(length2):
            row[a] = 0
            row[-(a+1)] = 0
            a += 1

for i in range(width):
    row = [1] * length
    num = 0
    if i < width2:
        cutout(num)
    num2 = 0
    if i >= (width - width2):
        cutout(num2)
    graph.append(row)
for j in range(width):
    graph[j].insert(0, 0)
    graph[j].append(0)

outline = [0] * (length +2)
graph.insert(0, outline)
graph.append(outline)

#Main Algorithm
pos = [1, length2+1 ]
top, right, bottom, left, num3, num4 = True, False, False, False, 2, 1

def fill(a,b):
    graph[a][b] = 0
def surround(a,b):
        if graph[a][b+1] == 0:
            if graph[a][b-1] == 0:
                if graph[a+1][b] == 0:
                    if graph[a-1][b] == 0:
                        return True


for p in range(steps):
    #Priority right, down
    fill(pos[0],pos[1])
    if top:
        if surround(pos[0],pos[1]):
            break
        if pos[1] == (length+2) - num3:
            top = False
            right = True
        else:
            if graph[pos[0]][pos[1]+1] != 0 and graph[pos[0]][pos[1]+1] != 0:
                pos[1] += 1
                fill(pos[0],pos[1])
            else:
                pos[0] += 1
                fill(pos[0],pos[1])
    #Priority down, left
    if right:
        if surround(pos[0],pos[1]):
            break
        if pos[0] == (width+2) - num3:
            right = False
            bottom = True
        else: 
            if graph[pos[0]+1][pos[1]] != 0 and graph[pos[0]+1][pos[1]] != 0:
                pos[0] += 1
                fill(pos[0],pos[1])
            else:
                pos[1] -= 1
                fill(pos[0],pos[1])
    #Priority left, up
    if bottom:
        if surround(pos[0],pos[1]):
            break
        if pos[1] == num4:
            bottom = False
            left = True
        else: 
            if graph[pos[0]][pos[1]-1] != 0 and graph[pos[0]][pos[1]-1] != 0:
                pos[1] -= 1
                fill(pos[0],pos[1])
            else:
                pos[0] -= 1
                fill(pos[0],pos[1])
    #Priority up, right
    if left:
        if surround(pos[0],pos[1]):
            break
        if pos[0] == num3:
            left = False
            top = True
            num3 += 1
            num4 += 1
        else: 
            if graph[pos[0]-1][pos[1]] != 0 and graph[pos[0]-1][pos[1]] != 0:
                pos[0] -= 1
                fill(pos[0],pos[1])
            else:
                pos[1] += 1
                fill(pos[0],pos[1])
        if pos[0] == num3:
            left = False
            top = True
            num3 += 1
            num4 += 1
            
print(pos[1])
print(pos[0])