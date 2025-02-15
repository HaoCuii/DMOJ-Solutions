user_input, stored_index, boolean, counter = list(input()), [], 0, 0

def check(x):
    global stored_index, boolean
    integer = []
    for j in range(len(user_input)):
        if counter + j +1 == len(user_input):
            break
        if user_input[counter + j + 1].isdigit():
            integer.append(user_input[counter + j + 1])
        else:
            break
    print(''.join(map(str, stored_index)), x, ''.join(map(str, integer)))
    stored_index, boolean = [], len(integer)

for i in user_input:
    if i == '-':
        check('loosen')
    elif i == '+':
        check('tighten')
    elif boolean < 1:
        stored_index.append(i)
    else:
        boolean -= 1
    counter += 1
