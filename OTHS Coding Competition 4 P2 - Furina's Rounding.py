n = input().strip()

if n[0] != '0' and n[1:] == '0' * (len(n) - 1):
    print('0')
else:
    rounded = str(int(n[0]) + 1) + '0' * (len(n) - 1)
    n = n.rjust(len(rounded), '0')

    res = []
    carry = 0
    for i in range(len(rounded) - 1, -1, -1):
        rd = int(rounded[i])
        nd = int(n[i])
        diff = rd - nd - carry
        if diff < 0:
            diff += 10
            carry = 1
        else:
            carry = 0
        res.append(str(diff))

    adjustment = ''.join(res[::-1]).lstrip('0') or '0'
    print(adjustment)
