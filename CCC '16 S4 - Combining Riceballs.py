import sys
input = sys.stdin.readline
n = int(input())
sum = [0]
riceballs = list(map(int,input().split()))

for i in range(n):
    sum.append(riceballs[i]+sum[i])
def get_sum(i, j):
    return sum[j + 1] - sum[i]

#state is the largest sum in the range i,j
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = riceballs[i]

#loop through all possible lengths of subarray
for length in range(2,n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        l,r = i,j

        while l < r:
            left_sum = get_sum(i, l)
            right_sum = get_sum(r, j)
            if left_sum < right_sum:
                l += 1  
            elif left_sum > right_sum:
                r -= 1
            else:
                if (dp[l+1][r-1] or l == r-1) and dp[i][l] and dp[r][j]:
                    dp[i][j] = get_sum(i,j)
                l += 1
                r -= 1

biggest = 0   
for i in dp:
    for j in i:
        biggest = max(biggest,j)
print(biggest)



            



    

    


    


    