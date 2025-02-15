x = int(input())

def recurse(depth,string,one):
    if depth == n:
        if one == k:
            print(string)
        return
    if one != k:
        recurse(depth+1,string+'1',one+1)
    recurse(depth+1,string+'0',one)
    

for i in range(x):
    n,k = map(int,input().split())
    print('The bit patterns are')
    recurse(0,'',0)
    if i != x-1
        print('')

