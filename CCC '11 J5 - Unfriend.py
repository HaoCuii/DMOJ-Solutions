'''
n = int(input())
dp = [1 for _ in range(n+1)]
for i in range(1,n):
    j = int(input())
    dp[j] *= (dp[i] + 1)
print(dp[n])
'''

def count_good_subsets(sample, m):
    goods = 0
    n = len(sample)

    # Generate all contiguous subsets
    for start in range(n):
        seen = set()  # To track unique elements
        for end in range(start, n):
            # If a duplicate is found, break early
            if sample[end] in seen:
                break
            seen.add(sample[end])

            # If any element is greater than m, break early
            if sample[end] > m:
                break

            # If the subset is valid, count it
            goods += 1
    
    return goods

# Example usage
m = 5
sample = [1, 2, 3, 4, 1]
result = count_good_subsets(sample, m)
print(result)


