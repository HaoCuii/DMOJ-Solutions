N = int(input())
platforms = []
for i in range(N):
    y, x1, x2 = map(int, input().split())
    platforms.append((y, x1, x2))

platforms = sorted(platforms)

total = 0
for i, (y, x1, x2) in enumerate(platforms):
    left_pillar = y
    right_pillar = y 
    
    for j in range(i):
        py, px1, px2 = platforms[j]
        if px1 <= x1 < px2 and py < y:
            left_pillar = min(left_pillar, y - py)
        if px1 < x2 <= px2 and py < y:
            right_pillar = min(right_pillar, y - py)
    
    total += left_pillar + right_pillar

print(total)