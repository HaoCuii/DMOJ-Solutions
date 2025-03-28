d = int(input())
q = int(input())
for i in range(q):
    o = str(input())
    n = int(input())
    if o == '+':
        d += n
    else:
        d -= n

print(d)