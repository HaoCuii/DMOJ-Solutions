'''
Ac uses c++ and a multiset, therefore append is logn,    remove is logn, max and min are all logn
Updating the sum can be done in constant time with a sum initialized at the start and updated
Therefore overall time complexity will be O(qlogn)
'''

n, m, q = map(int, input().split())
pens = [0]
color_prettyest, color_prettyest[0] = [0] * (m + 1), float('inf')
color_2prettyest = [0] * (m + 1)
colors_pretty = [[] for _ in range(m + 1)]

for i in range(n):
    c, p = map(int, input().split())
    if p > color_prettyest[c]:
        color_2prettyest[c] = color_prettyest[c]
        color_prettyest[c] = p
    else:
        color_2prettyest[c] = max(color_2prettyest[c], p)

    colors_pretty[c].append([p, i + 1])
    pens.append([c, p])

lowest_first = min(color_prettyest)
highest_second = max(color_2prettyest)

for i in range(q + 1):
    if i != 0:
        t, pen, pc = map(int, input().split())

        if t == 1:  # Change pen color
            old_color = pens[pen][0]
            new_color = pc

            # Remove from old color
            colors_pretty[old_color].remove([pens[pen][1], pen])
            if colors_pretty[old_color]:
                a, b = 0, 0
                for pair in colors_pretty[old_color]:
                    if pair[0] > a:
                        b = a
                        a = pair[0]
                    else:
                        b = max(b, pair[0])
                color_prettyest[old_color], color_2prettyest[old_color] = a, b
            else:
                color_prettyest[old_color] = 0
                color_2prettyest[old_color] = 0

            # Add to new color
            pens[pen][0] = new_color  
            colors_pretty[new_color].append([pens[pen][1], pen])

            a, b = 0, 0
            for pair in colors_pretty[new_color]:
                if pair[0] > a:
                    b = a
                    a = pair[0]
                else:
                    b = max(b, pair[0])
            color_prettyest[new_color], color_2prettyest[new_color] = a, b

        else:  # Change pen prettiness
            old_color = pens[pen][0]
            colors_pretty[old_color].remove([pens[pen][1], pen])
            pens[pen][1] = pc
            colors_pretty[old_color].append([pc, pen])

            a, b = 0, 0
            for pair in colors_pretty[old_color]:
                if pair[0] > a:
                    b = a
                    a = pair[0]
                else:
                    b = max(b, pair[0])
            color_prettyest[old_color], color_2prettyest[old_color] = a, b

        lowest_first = min(color_prettyest)
        highest_second = max(color_2prettyest)

    color_prettyest[0] = 0
    total = sum(color_prettyest)
    color_prettyest[0] = float('inf')
    
    if highest_second > lowest_first:
        total = total - lowest_first + highest_second
        
    print(total)
