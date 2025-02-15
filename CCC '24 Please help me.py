''' 
r = int(input())
g = int(input())
b = int(input())
total = 0
total += (r*3)
total += (g*4)
total += (b*5)
print(total)
'''
size = int(input())
while True:
    x = int(input())
    if size < x:
        break
    else:
        size += x
print(size)
