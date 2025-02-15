length = 5
updates = [
    [1, 3, 2], 
    [2, 4, 3],
    [0, 2, -2]  
]

arr = [1,2,3,4,5,0]
        
for v in updates:
    arr[v[0]] += v[2]
    if v[1] + 1 < len(arr):
        arr[v[1] + 1] -= v[2]
        
for i in range(1, length):
    arr[i] += arr[i - 1]
        
arr.pop()

print(arr)