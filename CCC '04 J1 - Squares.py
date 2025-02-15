import math
Number = int(input())
i = 0
while i < Number:
    SquareRooted = math.sqrt(Number)
    if SquareRooted == int(SquareRooted):
        print("The largest square has a side length "+str(int(SquareRooted))+".")
        break
    else:
        Number -= 1
