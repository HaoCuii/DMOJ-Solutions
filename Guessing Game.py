import sys
import math
Start_val = 500000000
while True:
    print(Start_val)
    x = int(input())
    if x == 0:
        sys.exit()
    Start_val += math.floor(x/2)


