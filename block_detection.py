def user_solution(n, wil, kev, a, b, c, d):
    count = {'A':a, 'B':b, 'C':c, 'D':d}
    total = 0
    new = []
    for i in range(n):
        if kev[i] != '?':
            count[kev[i]] -= 1
            if wil[i] == kev[i]:
                total += 1
        else:
            new.append(wil[i])
    A, B, C, D = new.count('A'), new.count('B'), new.count('C'), new.count('D')
    largest = sorted(count.items(), key=lambda item: item[1], reverse=True)
    
    # Replicate the original logic with globals()
    global_A = A
    global_B = B
    global_C = C
    global_D = D
    
    for i in range(4):
        ans, cnt = largest[i]
        for j in range(i+1, 4):
            ans2, cnt2 = largest[j]
            if ans2 == 'A': var = global_A
            elif ans2 == 'B': var = global_B
            elif ans2 == 'C': var = global_C
            else: var = global_D
            temp = var - min(var, cnt)
            if var > cnt:
                cnt = 0
                break
            else:
                cnt -= var
            var = temp
            if ans2 == 'A': global_A = var
            elif ans2 == 'B': global_B = var
            elif ans2 == 'C': global_C = var
            else: global_D = var
        for j in range(i):
            ans2, cnt2 = largest[j]
            if ans2 == 'A': var = global_A
            elif ans2 == 'B': var = global_B
            elif ans2 == 'C': var = global_C
            else: var = global_D
            temp = var - min(var, cnt)
            if var > cnt:
                cnt = 0
                break
            else:
                cnt -= var
            var = temp
            if ans2 == 'A': global_A = var
            elif ans2 == 'B': global_B = var
            elif ans2 == 'C': global_C = var
            else: global_D = var
        if cnt > 0:
            if ans == 'A': 
                global_A -= cnt
                total += cnt
            elif ans == 'B': 
                global_B -= cnt
                total += cnt
            elif ans == 'C': 
                global_C -= cnt
                total += cnt
            else: 
                global_D -= cnt
                total += cnt
    return total

def correct_solution(n, wil, kev, a, b, c, d):
    count = {'A':a, 'B':b, 'C':c, 'D':d}
    total = 0
    unknowns = []
    for i in range(n):
        if kev[i] == '?':
            unknowns.append(wil[i])
        else:
            count[kev[i]] -= 1
            if wil[i] == kev[i]:
                total += 1
    freq = {'A':0, 'B':0, 'C':0, 'D':0}
    for c in unknowns:
        freq[c] += 1
    for letter in 'ABCD':
        avoidable = len(unknowns) - freq[letter]
        forced = max(0, count[letter] - avoidable)
        total += forced
    return total

import itertools

def generate_valid_test_case(n):
    # Create a list to store all the valid test cases
    count = 0
    for kev in itertools.product(['A', 'B', 'C', 'D', '?'], repeat=n):
        for wil in itertools.product(['A', 'B', 'C', 'D'], repeat=n):
            # Count the occurrences of 'A', 'B', 'C', 'D' in wil
            a = wil.count('A')
            b = wil.count('B')
            c = wil.count('C')
            d = wil.count('D')
            
            # Count occurrences in kev
            kev_count = {'A': kev.count('A'), 'B': kev.count('B'), 'C': kev.count('C'), 'D': kev.count('D')}
            
            # Make sure kev counts for A, B, C, D are >= counts in wil
            if kev_count['A'] >= a and kev_count['B'] >= b and kev_count['C'] >= c and kev_count['D'] >= d:
                # Yield the test case with a total of generated test cases
                yield n, list(wil), list(kev), a, b, c, d
                count += 1
                if count >= 1000000:  # Stop after 1 million test cases
                    return

def stress_test():
    case = 0
    # Loop over the sizes from 1 to 7
    for n in range(1, 8):  # Sizes from 1 to 7
        test_cases = generate_valid_test_case(n)
        
        # Run stress test for each size, up to 1,000,000 test cases
        for n, wil, kev, a, b, c, d in test_cases:
            case += 1
            user_ans = user_solution(n, wil, kev, a, b, c, d)
            correct_ans = correct_solution(n, wil, kev, a, b, c, d)
            if user_ans != correct_ans:
                print("Discrepancy found!")
                print(f"n = {n}")
                print(f"Wil's answers: {''.join(wil)}")
                print(f"Kev's answers: {''.join(kev)}")
                print(f"Counts (a, b, c, d): {a} {b} {c} {d}")
                print(f"Your output: {user_ans}")
                print(f"Correct output: {correct_ans}")
                break  # Exit on the first discrepancy
            else:
                print(f"Case {case}: OK {n}")

# Run the test
stress_test()


