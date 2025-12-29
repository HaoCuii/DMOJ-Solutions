import sys
import random
rand = random.SystemRandom()

num = int(input())

if num == 1:
    print(2)
    sys
elif num == 2:
    print(2)
elif num == 3:
    print(3)
else:
    def a_test(n,a):
        exp = n-1

        while not exp & 1: #while exp is even
            exp >>= 1 #exp //= 2

        if pow(a,exp,n) == 1: #a**exp % n (Mod n for big numbers)
            return True

        while exp < n - 1:
            if pow(a,exp,n) == n - 1: # == -1 
                return True
            
            exp <<= 1 #exp *= 2

        return False

    def miller_rabin(n,k=3): #k is number of values of a

        for _ in range(k):
            a = rand.randrange(2, n-1) #Non inclusive

            if not a_test(n,a):
                return False
        
        return True


    for i in range(num, sys.maxsize):
        if miller_rabin(i):
            print(i)
            break