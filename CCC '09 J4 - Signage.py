line_len = int(input())
line_len2 = line_len
text = ['WELCOME','TO', 'CCC','GOOD','LUCK','TODAY']
output = []
counter2 = 0
def period(counter,i,line_len2):
    line_len2 += i
    for j in range(line_len2):
            global output, counter2
            num = 0
            if counter+1 >= len(output) and len(output) != 1:
                counter = 1 
                num += 1
                output.insert(counter+1,'.')
                counter += 2 + num
            else:
                output.insert(counter+1,'.')
                counter += 2 + num
    counter2 = 0
    print(''.join(output))
for i in text:
    counter = 0
    if (line_len2 - (len(list(i))+1)) >= -1:
        line_len2 -= (len(list(i))+1)
        output.append(i)
    else:
        period(counter,counter2,line_len2)
        output = []
        line_len2 = line_len
        if (line_len2 - (len(list(i))+1)) >= 0:
            line_len2 -= (len(list(i))+1)
            output.append(i)
    counter2+=1
    if i == 'TODAY':
        period(counter,counter2,line_len2)