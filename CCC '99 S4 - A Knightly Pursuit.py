from collections import deque
for i in range(int(input())):
    r,c,pr,pc,kr,kc = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
    queue = deque([(pr,pc,kr,kc,0)])
    visited = set()
    w = []
    d = []
    s = []
    while queue:
        pr,pc,kr,kc,m = queue.popleft()
        if (pr,pc) == (kr,kc):
            w.append(m)
            break
        npr,npc = pr+1,pc
        if npr > r:
            break
        if (npr,npc) == (kr,kc):
            d.append(m)
        if npr == r:
            s.append(m)
        kdirections = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for i in kdirections:
            nkr,nkc = kr+i[0],kc+i[1]
            if 1 <= nkr <= r and 1 <= nkc <= c and (nkr,nkc,m) not in visited:
                visited.add((nkr,nkc,m))
                queue.append((npr,npc,nkr,nkc,m+1))

    if len(w) > 0:
        print('Win in',w[0],'knight move(s).')
    elif len(d) > 0:
        print('Stalemate in',d[0],'knight move(s).')
    else:
        print('Loss in',s[0],'knight move(s).')