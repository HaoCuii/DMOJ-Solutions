n = int(input())

for i in range(n):
    code = str(input())
    total = 0
    new_code = []
    idx = 0
    while idx < len(code):
        if code[idx] == '-':
            idx += 1
            num = ''
            while True:
                if idx == len(code) or not code[idx].isdigit():
                    break
                num += code[idx]
                idx += 1
            total -= int(num)
        elif not code[idx].isdigit():
            if code[idx] == code[idx].upper():
                new_code.append(code[idx])
            idx += 1
        else:
            num = ''
            while True:
                if idx == len(code) or not code[idx].isdigit():
                    break
                num += code[idx]
                idx += 1
            total += int(num)
    new_code.append(total)
    print(''.join(map(str,new_code)))
