import sys
n,m,k = map(int,input().split())

if k >= n and k <= (n*(n+1))/2:
    if n == k:
        l = ['1' for i in range(n)]
        print(' '.join(l))
        sys.exit()

    new_m = 1
    for i in range(1,n+1):
        if i+1 > m:
            print(-1)
            sys.exit()
        if  k <= n + (i*(i+1)/2) + (n-i-1)*(i-1+1):
            new_m = i+1
            break  
    arr = []
    total = n + (new_m*(new_m-1)//2)
    last_val = -1

    for i in range(n):
        if last_val != -1:
            arr.append(last_val)
        elif i < new_m:
            arr.append(i%new_m+1)
        elif total + new_m-1 <= k:
            total += new_m-1
            arr.append(i%new_m+1) 
        else:
            last_val = arr[-(k-total)-1]
            arr.append(arr[-(k-total)-1])
    print(' '.join(map(str,arr)))
else:
    print(-1)