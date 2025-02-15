length = int(input())
line1 = input()
line2 = input()
line1,line2 = list(line1.replace(' ', '')),list(line2.replace(' ', ''))
lines = 0
for i in range(length):
    if line1[i] == '1':
        lines += 3
        if i % 2 == 0 and line2[i] == '1':
            lines -= 1
        if i < (length-1) and line1[i+1] == '1':
            lines -= 1
        if i > 0 and line1[i-1] == '1':
            lines -= 1
for i in range(length):
    if line2[i] == '1':
        lines += 3
        if i % 2 == 0 and line1[i] == '1':
            lines -= 1
        if i < (length-1) and line2[i+1] == '1':
            lines -= 1
        if i > 0 and line2[i-1] == '1':
            lines -= 1
print(lines)