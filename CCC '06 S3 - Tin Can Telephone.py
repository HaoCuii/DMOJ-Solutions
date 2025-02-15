xr, yr, xj, yj = map(int, input().split())
n = int(input())

# Calculate the slope and intercept of the main line
if xr != xj:
    m = (yr - yj) / (xr - xj)
    b = yr - m * xr
else:
    # Handle vertical main line
    m = None
    b = None

touching = 0

for _ in range(n):
    c = list(map(int, input().split()))
    corners = []
    for i in range(1, c[0] * 2 + 1, 2):
        corners.append((c[i], c[i + 1]))
    
    lines = []
    for i in range(len(corners)):
        (x1, y1) = corners[i]
        (x2, y2) = corners[0]
        if i != len(corners) - 1:
            (x2, y2) = corners[i + 1]
        
        if x1 != x2:
            m2 = (y1 - y2) / (x1 - x2)
            b2 = y1 - m2 * x1
            lines.append((m2, b2, x1, y1, x2, y2, False))  # False indicates not vertical
        else:
            lines.append((None, None, x1, y1, x2, y2, True))  # True indicates vertical

    for (m2, b2, x1, y1, x2, y2, is_vertical) in lines:
        if is_vertical:
            if m is not None:
                x_intersect = x1
                y_intersect = m * x_intersect + b
                if (max(min(xr, xj), min(x1, x2)) <= x_intersect <= min(max(xr, xj), max(x1, x2))) and (max(min(yr, yj), min(y1, y2)) <= y_intersect <= min(max(yr, yj), max(y1, y2))):
                    touching += 1
                    break
            else:
                if x1 == xr:
                    if not (max(y1, y2) < min(yr, yj) or min(y1, y2) > max(yr, yj)):
                        touching += 1
                        break
        else:
            if m is not None:
                if m2 != m:
                    x_intersect = (b2 - b) / (m - m2)
                    y_intersect = m * x_intersect + b
                    if (max(min(xr, xj), min(x1, x2)) <= x_intersect <= min(max(xr, xj), max(x1, x2))) and (max(min(yr, yj), min(y1, y2)) <= y_intersect <= min(max(yr, yj), max(y1, y2))):
                        touching += 1
                        break
            else:
                x_intersect = xr
                y_intersect = m2 * x_intersect + b2
                if (max(min(xr, xj), min(x1, x2)) <= x_intersect <= min(max(xr, xj), max(x1, x2))) and (max(min(yr, yj), min(y1, y2)) <= y_intersect <= min(max(yr, yj), max(y1, y2))):
                    touching += 1
                    break

print(touching)