
r = int(input())  
c = int(input())  
graph = []
wall_pos = []

for i in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            wall_pos.append((i, j))

m = int(input())  
inputs = [input() for _ in range(m)]

direction_transitions = {
    'U': {'L': 'L', 'R': 'R'},
    'L': {'L': 'D', 'R': 'U'},
    'R': {'L': 'U', 'R': 'D'},
    'D': {'L': 'R', 'R': 'L'}
}

grid_transitions = {
    'U': (-1, 0),
    'L': (0, -1),
    'R': (0, 1),
    'D': (1, 0)
}

def generate_paths(direction):
    previous_grid = [0, 0]
    grid_traveled = set()
    grid_traveled.add((0, 0))


    top = 0
    bottom = 0
    left = 0
    right = 0
    
    for move in inputs:
        if move == 'F':
            previous_grid[0] += grid_transitions[direction][0]
            previous_grid[1] += grid_transitions[direction][1]
            grid_traveled.add(tuple(previous_grid))
            
            # Update extreme values
            top = min(top, previous_grid[0])
            bottom = max(bottom, previous_grid[0])
            left = min(left, previous_grid[1])
            right = max(right, previous_grid[1])
        else:
            direction = direction_transitions[direction][move]
    
    return (
        tuple(previous_grid), 
        grid_traveled, 
        (top, bottom, left, right)  # Return extreme values
    )

# Example usage
final_pos_U, grid_traveled_U, bounds_U = generate_paths('U')
final_pos_D, grid_traveled_D, bounds_D = generate_paths('D')
final_pos_L, grid_traveled_L, bounds_L = generate_paths('L')
final_pos_R, grid_traveled_R, bounds_R = generate_paths('R')

def search(i, j, final_pos, grid_traveled, bounds):
    top, bottom, left, right = bounds  
    if (
        top + i >= 0 and bottom + i < r and 
        left + j >= 0 and right + j < c  
    ):
        wall_in_way = False
        for a, b in wall_pos: 
            wall_prop = (a - i, b - j)
            if wall_prop in grid_traveled:
                wall_in_way = True
                break
        if not wall_in_way:
            graph[i + final_pos[0]][j + final_pos[1]] = '*'

for i in range(r):
    for j in range(c):
        search(i, j, final_pos_U, grid_traveled_U, bounds_U)
        search(i, j, final_pos_D, grid_traveled_D, bounds_D)
        search(i, j, final_pos_L, grid_traveled_L, bounds_L)
        search(i, j, final_pos_R, grid_traveled_R, bounds_R)


for row in graph:
    print(''.join(row))


