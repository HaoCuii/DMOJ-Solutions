from collections import deque

inputs = list(input())
move = 0
index_l, index_m, index_s = [], [], []

for i, char in enumerate(inputs):
    if char == 'L':
        index_l.append(i)
    elif char == 'M':
        index_m.append(i)
    elif char == 'S':
        index_s.append(i)

index_l2 = index_l

# Convert index_s and index_m to deques
index_s = deque(index_s)
index_m = deque(index_m)

for i in range(len(index_l)):
    if index_l[-(i+1)] >= len(index_l):
        if len(index_s) != 0:
            j = index_s[0]
        if len(index_m) != 0:
            k = index_m[0]
        if len(index_s) != 0 and j < len(index_l):
            inputs[index_l[-(i+1)]], inputs[j] = inputs[j], inputs[index_l[-(i+1)]]
            move += 1
            index_s.popleft()
        elif len(index_m) != 0 and k < len(index_l):
            inputs[index_l[-(i+1)]], inputs[k] = inputs[k], inputs[index_l[-(i+1)]]
            move += 1
            index_m.popleft()
    else:
        break

index_m, index_s = deque(), deque()

for i in range(len(index_l), len(inputs)):
    if inputs[i] == 'S':
        index_s.append(i)
    elif inputs[i] == 'M':
        index_m.append(i)

for i in range(len(index_s)):
    if index_s[i] < len(index_s) + len(index_l2):
        if len(index_m) != 0:
            j = index_m[-1]
        if len(index_m) != 0 and j >= len(index_m) + len(index_l2):
            inputs[index_s[i]], inputs[j] = inputs[j], inputs[index_s[i]]
            move += 1
            index_m.pop()
        break

index_m, index_s = deque(), deque()

for i in range(len(index_l), len(inputs)):
    if inputs[i] == 'S':
        index_s.append(i)
    elif inputs[i] == 'M':
        index_m.append(i)

for i in range(len(index_m)):
    if index_m[-(i+1)] >= len(index_m) + len(index_l2):
        if len(index_s) != 0:
            j = index_s[0]
        if len(index_s) != 0 and j < len(index_m) + len(index_l2):
            inputs[index_m[-(i+1)]], inputs[j] = inputs[j], inputs[index_m[-(i+1)]]
            move += 1
            index_s.popleft()
    else:
        break

print(move)
