values = []
while 1:
    user_input = input()
    if user_input == '0':
        break
    values.append(user_input.split())
for i in values:
    counter = 2
    for j in range(len(i)):
        if i[-(j+1)] == '-' or i[-(j+1)] == '+':
            if -(j-1) <= len(i) and i[-j] not in ['+','-'] and i[-(j-1)] not in ['+','-']:
                z = i.pop(-(j+1))
                if (-j)+2 == 0:
                    i.append(z)
                else:
                    i.insert((-j)+2, z)
                counter += 2
            else:
                z = i.pop(-(j+1))
                if (-j)+counter == 0:
                    i.append(z)
                else:
                    i.insert((-j)+counter, z)
                counter += 2
    print(' '.join(i))