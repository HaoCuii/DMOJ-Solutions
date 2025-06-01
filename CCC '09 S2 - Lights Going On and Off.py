r = int(input())
l = int(input())
seen = set()

bottom = int(''.join(input().split()), 2)
seen.add(bottom)
for i in range(r-1):
    row = int(''.join(input().split()), 2)
    bottom = bottom ^ row
    seen.add(bottom)

print(len(seen))
