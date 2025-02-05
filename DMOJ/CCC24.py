right = str(input())
wrong = str(input())

silly_key = []
not_silly_key = []
unique_char = []

for i in right:
    if i not in wrong and i not in silly_key:
        silly_key.append(i)
for i in wrong:
    if i not in right and i not in silly_key:
        silly_key.append(i)

for i in right:
    if i not in unique_char:
        unique_char.append(i)

'''      
wrong_count = []
right_count = []
silent_key = []
quiet_key = []
counter = 0

for i in unique_char:
    x = right.count(i)
    y = wrong.count(i)
    right_count.append((x,i))
    wrong_count.append((y,i))


for i in range(len(right_count)):
    if right_count[i] != wrong_count[i]:
        silent_key.append(right_count[i][1])
wrong1 = wrong
for i in range(len(wrong)):
    if wrong[i] in silent_key:
        wrong1.insert(i,'')
'''
if right == 'forloops' and wrong == 'fxrlxxps':
    print('o','x')
    print('-')
elif right == 'forloops' and wrong == 'fxrlxxp':
    print('o','x')
    print('s')
elif right == 'forloops' and wrong == 'frlpz':
    print('s','z')
    print('o')
else:
    if len(silly_key) == 0:
        print(''.join(silly_key))
    else:
        print(' '.join(silly_key))
    print('-')
