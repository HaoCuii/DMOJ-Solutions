word = list(str(input()))
row, col = int(input()), int(input())
word_grid = []
word_instances = 0
for i in range(row):
    word_grid.append(list(''.join(str(input()).split())))
def recursion(word_grid,row1,col2,visited,counter,multiplier1,multiplier2, has_turned):
    global word_instances
    if -1 < row1 < row and -1 < col2 < col and (row1,col2) not in visited:
        if word_grid[row1][col2] == word[-1] and counter == (len(word)-1):
            word_instances += 1
            return
        if word_grid[row1][col2] == word[counter] and counter > 0:
            counter += 1
            visited.append((row1,col2))
            if multiplier1 == 0 or multiplier2 == 0:
                if has_turned:
                    recursion(word_grid.copy(), row1+(1*multiplier2), col2-(1*multiplier1),visited.copy(),counter,(1*multiplier2),-(1*multiplier1),False)
                    recursion(word_grid.copy(), row1-(1*multiplier2), col2+(1*multiplier1),visited.copy(),counter,-(1*multiplier2),(1*multiplier1),False)
                recursion(word_grid.copy(), row1+(1*multiplier1), col2+(1*multiplier2),visited.copy(),counter,1*multiplier1,1*multiplier2,has_turned)
            elif multiplier1 == multiplier2:
                if has_turned:
                    recursion(word_grid.copy(), row1+(1*multiplier1), col2-(1*multiplier2),visited.copy(),counter,(1*multiplier1),-(1*multiplier2),False)
                    recursion(word_grid.copy(), row1-(1*multiplier1), col2+(1*multiplier2),visited.copy(),counter,-(1*multiplier1),(1*multiplier2),False)
                recursion(word_grid.copy(), row1+(1*multiplier1), col2+(1*multiplier2),visited.copy(),counter,1*multiplier1,1*multiplier2,has_turned)
            else:
                if has_turned:
                    recursion(word_grid.copy(), row1+(1*multiplier1), col2-(1*multiplier2),visited.copy(),counter,+(1*multiplier1),-(1*multiplier2),False)
                    recursion(word_grid.copy(), row1-(1*multiplier1), col2+(1*multiplier2),visited.copy(),counter,-(1*multiplier1),+(1*multiplier2),False)
                recursion(word_grid.copy(), row1+(1*multiplier1), col2+(1*multiplier2),visited.copy(),counter,1*multiplier1,1*multiplier2,has_turned)
        else:
            if word_grid[row1][col2] == word[counter]:
                counter += 1
                visited.append((row1,col2))
                recursion(word_grid.copy(), row1+1, col2,visited.copy(),counter,1,0, has_turned)
                recursion(word_grid.copy(), row1-1, col2,visited.copy(),counter,-1,0,has_turned)
                recursion(word_grid.copy(), row1, col2-1,visited.copy(),counter,0,-1,has_turned)
                recursion(word_grid.copy(), row1, col2+1,visited.copy(),counter,0,1,has_turned)            
                recursion(word_grid.copy(), row1+1, col2+1,visited.copy(),counter,1,1,has_turned)
                recursion(word_grid.copy(), row1-1, col2-1,visited.copy(),counter,-1,-1,has_turned)
                recursion(word_grid.copy(), row1-1, col2+1,visited.copy(),counter,-1,1,has_turned)
                recursion(word_grid.copy(), row1+1, col2-1,visited.copy(),counter,1,-1,has_turned)
            else:
                return
for j in range(row):
    for k in range(col):
        if word_grid[j][k] == word[0]:
            visited = []
            counter = 0
            recursion(word_grid,j,k,visited,counter,0,0, True)
print(word_instances)


