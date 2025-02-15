N = int(input())

if N == 1:
    print('1')
elif N == 2:
    print(-1)
elif N == 3:
    print(-1)
elif N == 4:
    print(-1)
elif N == 5:
    print('2 4 5 3 1')
elif N == 6:
    print('2 6 4 5 3 1')
elif N == 7:
    print('2 6 4 5 3 1 7')
else:
    even = []
    odd = []

    for i in range(2,N+1,2):
        if i == 8:
            pass
        else:
            even.append(i)
    even.append(8)

    for i in range(1,N+1,2):
        odd.append(i)

    print(' '.join(map(str,(even+odd))))