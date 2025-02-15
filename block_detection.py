def touching_segments(x1, y1, x2, y2, x3, y3, x4, y4):
    def between(x, a, b):
        return min(a, b) <= x <= max(a, b)
    
    if x1 == x2:
        m1, b1 = float('inf'), 0
    else:
        m1 = (y1 - y2) / (x1 - x2)
        b1 = -m1 * x2 + y2
    
    if x3 == x4:
        m2, b2 = float('inf'), 0
    else:
        m2 = (y3 - y4) / (x3 - x4)
        b2 = -m2 * x4 + y4
    
    # Segments are parallel
    if m1 == m2:
        if m1 != float('inf') and m2 != float('inf'):
            return b1 == b2 and (between(x3, x1, x2) or between(x4, x1, x2))
        else:
            return x1 == x3 and (between(y3, y1, y2) or between(y4, y1, y2))
    else:
        if m1 != float('inf') and m2 != float('inf'):
            xi = (b2 - b1) / (m1 - m2)
            yi = m1 * xi + b1
        else:
            if m1 == float('inf'):
                xi = x1
                yi = m2 * xi + b2
            else:
                xi = x3
                yi = m1 * xi + b1
        return (between(xi, x1, x2) and between(yi, y1, y2) and 
                between(xi, x3, x4) and between(yi, y3, y4))


xr, yr, xj, yj = map(int, input().split())
n = int(input())
touch = 0

for _ in range(n):
    data = list(map(int, input().split()))
    corners = data[0]
    x0, y0 = data[1], data[2]
    x1, y1 = x0, y0
    touching = False
    
    for j in range(1, corners):
        x2, y2 = data[2 * j + 1], data[2 * j + 2]
        touching |= touching_segments(xr, yr, xj, yj, x1, y1, x2, y2)
        x1, y1 = x2, y2
    
    touching |= touching_segments(xr, yr, xj, yj, x1, y1, x0, y0)
    if touching:
        print(data)
        touch += 1

print(touch)

