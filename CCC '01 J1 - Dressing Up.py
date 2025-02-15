inp = int(input())
counter = 0
for i in range(inp):
    list = []
    counter2 = 0
    for j in range(inp*2):
        list.append(' ')
    for k in range(counter+1):
        list[counter2] = '*'
        list[-(counter2+1)] = '*'
        counter2 += 1
    if i > ((inp // 2)-1):
        counter -= 2
    else:
        counter += 2
    print(''.join(map(str,list)))