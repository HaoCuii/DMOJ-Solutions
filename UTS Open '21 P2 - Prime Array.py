'''
Only need 1's and 2's
Have a loop which sets the first i numbers to 2 (i from 0 to max)
For each loop set the remaining numbers every other one to 2 and make sure to check if it equals k for each one?
We loop through all lengths of the array as well 
'''
import sys
k = int(input())
if k == 0:
    print(1)
    print(2)
    sys.exit()
for n in range(1,101):
    for start in range(n+1):
        for cont in range(n-start):
            if (n*(n+1)//2 - (start*(start+1)//2) - (cont+1)//2 == k):
                print(n)
                for i in range(start):
                    print(2, end=" ")
                for i in range(cont+1):
                    if (i % 2 == 1):
                        print(2, end =" ")
                    else:
                        print(1, end = " ")
                for i in range(n-start-(cont+1)):
                    print(1, end=" ")
                sys.exit()



        
