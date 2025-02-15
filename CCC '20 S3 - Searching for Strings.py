import sys

needle = sys.stdin.readline().rstrip()
haystack = sys.stdin.readline().rstrip()

if len(needle) > len(haystack):
    print(0)
    sys.exit()

window_size = len(needle)
total = 0
q = 10e9 + 9
d = 26
p = 0
t = 0
h = 1

window_map = [0] * 26
needle_map = [0] * 26

def char_to_index(char):
    return ord(char) - ord('a')

for i in needle:
    needle_map[char_to_index(i)] += 1


for i in range(0, window_size):
    window_map[char_to_index(haystack[i])] += 1
seen_permutations = set()

for i in range(len(needle) - 1):
    h = (h * d) % q

for i in range(len(needle)):
    t = (d * t + (ord(haystack[i]) - ord('a') + 1)) % q

for i in range(242069):
    match = True
    if needle_map != window_map:
        match = False
    if i != 0:
        t = (d * (t - (ord(haystack[i - 1]) - ord('a') + 1) * h) % q + (ord(haystack[i + len(needle) - 1]) - ord('a') + 1)) % q
        if t < 0:
            t = t + q
    if match:
        if t not in seen_permutations:
            seen_permutations.add(t)
            total += 1

    if i + window_size >= len(haystack):
        break

    window_map[char_to_index(haystack[i])] -= 1
    window_map[char_to_index(haystack[i+len(needle)])] += 1

print(total)