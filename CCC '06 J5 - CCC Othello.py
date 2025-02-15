inp = input().split(" ")
case = inp[0]
moves = inp[1]
a = [[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,1,2,0,0,0],
     [0,0,0,2,1,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

b = [[2,0,0,0,0,0,0,1],
     [0,2,0,0,0,0,1,0],
     [0,0,2,0,0,1,0,0],
     [0,0,0,2,1,0,0,0],
     [0,0,0,1,2,0,0,0],
     [0,0,1,0,0,2,0,0],
     [0,1,0,0,0,0,2,0],
     [1,0,0,0,0,0,0,2]]

c = [[0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0],
     [0,0,2,2,1,1,0,0]]
if case == 'a':
    case = a
if case == 'b':
    case = b
if case == 'c':
    case = c
counter = 2
def check(col,row,row2,col2,multiplier,multiplier2,white,black):
    flipped_coords = []
    if col > 7 or col < 0 or row > 7 or row < 0:
        pass
    else:
        if case[row][col] == white:
            flipped_coords.append([row])
            flipped_coords.append([col])
            for i in range(8):
                if col2+(i*multiplier) > 7 or col2+(i*multiplier) < 0 or row2+(i*multiplier2) > 7 or row2+(i*multiplier2) < 0:
                    if i-1 < 0:
                        if case[row2+((i+1)*multiplier2)][col2+((i+1)*multiplier)] == white:
                                flipped_coords = []
                                break
                    else:
                        if case[row2+((i-1)*multiplier2)][col2+((i-1)*multiplier)] == white:
                            flipped_coords = []
                            break
                else:
                    if case[row2+(i*multiplier2)][col2+(i*multiplier)] == white:
                        flipped_coords.append([row2+(i*multiplier2)])
                        flipped_coords.append([col2+(i*multiplier)])
                    elif case[row2+(i*multiplier2)][col2+(i*multiplier)] == black:
                        break
                    else:
                        flipped_coords = []
                        break
    counter1 = 0
    for i in range(int(len(flipped_coords)/2)):
        case[flipped_coords[counter1][0]][flipped_coords[counter1+1][0]] = black
        counter1 += 2
for i in range(int(moves)):
    row, col = int(inp[counter]), int(inp[counter+1])
    counter += 2
    flipped_coords = []
    if i % 2 == 0:
        case[row-1][col-1] = 2
        check(col-2, row-1, row-1, col-3, -1, 0, 1, 2)
        check(col, row-1, row-1, col+1, 1, 0, 1, 2)
        check(col-1, row-2, row-3, col-1, 0, -1, 1, 2)
        check(col-1, row, row+1, col-1, 0, 1, 1, 2)
        check(col-2, row-2, row-3, col-3, -1, -1, 1, 2)
        check(col-2, row, row+1, col-3, -1, -1, 1, 2)
        check(col, row-2, row-3, col+1, 0, 0, 1, 2)
        check(col, row, row+1, col+1, 0, 0, 1, 2)    
    else:
        case[row-1][col-1] = 1
        check(col-2, row-1, row-1, col-3, -1, 0, 2, 1)
        check(col, row-1, row-1, col+1, 1, 0, 2, 1)
        check(col-1, row-2, row-3, col-1, 0, -1, 2, 1)
        check(col-1, row, row+1, col-1, 0, 1, 2, 1)
        check(col-2, row-2, row-3, col-3, -1, -1, 2, 1)
        check(col-2, row, row+1, col-3, -1, -1, 2, 1)
        check(col, row-2, row-3, col+1, 0, 0, 2, 1)
        check(col, row, row+1, col+1, 0, 0, 2, 1)
black, white = [], []
for m in case:
    for n in m:
        if n == 2:
            black.append(n)
        if n == 1:
            white.append(n)
print(len(black), len(white))


