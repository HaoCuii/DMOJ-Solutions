inputs = []
counter = 0
counter2 = 0
while 1:
    a = int(input())
    if a == 99 and counter2 < 1:
        counter2 = 3
    if a == 88 and counter2 < 1:
        counter2 = 2
    if a == 77 and counter2 < 1:
        break
    inputs.append(a)
    counter += 1
    counter2 -= 1
rivers = []
for i in range(inputs[0]):
    rivers.append(inputs[i+1])
for i in range(len(inputs)):
    if inputs[i] == 99 and counter2 < 1:
        split_val = rivers[inputs[i+1]-1]
        left_val, right_val = split_val*(inputs[i+2]/100), split_val*(1-(inputs[i+2]/100))
        rivers[inputs[i+1]-1] = left_val
        rivers.insert(inputs[i+1], right_val)
        counter2 = 3
    elif inputs[i] == 88 and counter2 < 1:
        added_val = rivers[inputs[i+1]-1]+rivers[inputs[i+1]]
        rivers[inputs[i+1]-1] = added_val
        rivers.pop(inputs[i+1])
        counter2 = 2
    counter2 -= 1
rivers_final = []
for i in rivers:
    rivers_final.append(round(i))
print(' '.join(map(str,rivers_final)))

