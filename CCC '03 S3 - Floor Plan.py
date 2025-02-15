supply, rows_input, columns_input, floor_plan, rooms, counter = int(input()), int(input()), int(input()), [], [], 0
for i in range(rows_input):
    floor_plan.append(list(input()))
def dfs(grid, row, col, visited):
    global room_size
    rows, cols = rows_input, columns_input
    if (row, col) not in visited and grid[row][col] == '.' and 0 <= col < cols and 0 <= row < rows:
        visited.add((row, col))
        grid[row][col] = 'I'
        room_size += 1
        dfs(grid, row-1, col, visited)
        dfs(grid, row+1, col, visited)
        dfs(grid, row, col-1, visited)
        dfs(grid, row, col+1, visited)
for j in floor_plan:
    for k in range(len(j)):
        if floor_plan[counter][k] == '.':
            room_size, visited = 0, set()
            dfs(floor_plan, counter, k, visited)
            rooms.append(room_size)
    counter += 1
sorted_rooms, filled_rooms = sorted(rooms, reverse=True), []
for l in range(len(sorted_rooms)):
    if supply - sorted_rooms[l] < 0:
        break
    else:
        supply -= sorted_rooms[l]
        filled_rooms.append(sorted_rooms[l])
if len(filled_rooms) == 1 :
    print(len(filled_rooms), 'room,', supply, 'square metre(s) left over')
else:
    print(len(filled_rooms), 'rooms,', supply, 'square metre(s) left over')
