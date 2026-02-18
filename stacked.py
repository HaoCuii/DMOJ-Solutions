#TIME TO IMPLEMENT WITH 1000WPM
N = int(input())
s1 = list(map(int, input().split()))
s2 = []
nxt = 1
moves = []
S = set(s1)

while nxt <= N:
    if s1 and s1[-1] == nxt:
        moves.append("1 3")
        S.discard(s1.pop())
        nxt += 1
    elif s2 and s2[-1] == nxt:
        moves.append("2 3")
        s2.pop()
        nxt += 1
    elif nxt in S:
        moves.append("1 2")
        S.discard(s1[-1])
        s2.append(s1.pop())
    else:
        moves.append("2 1")
        S.add(s2[-1])
        s1.append(s2.pop())

print(len(moves))
print('\n'.join(moves))