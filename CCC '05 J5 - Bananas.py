def function(start_pos, end_pos, lis):
    global bool2
    bool_var, b_bool = False, False
    for i in lis[start_pos:end_pos + 1]:
        if i == 'A' and not bool_var:
            bool_var = True
        elif i == 'B' and not bool_var:
            b_bool = True
        elif i == 'N' and bool_var:
            bool_var = False
        else:
            if b_bool and i == 'S' and bool_var:
                b_bool = False
            else:
                bool2 = False
                return
    if not bool_var:
        bool2 = False
        return
    lis[start_pos:end_pos + 1] = 'A'

def recursion(lis):
    global bool2
    if lis == ['A']:
        print('YES')
        return
    b_index = 0
    s_index = len(lis)
    bool2 = True

    for i in range(len(lis)):
        if lis[i] == 'B':
            b_index = i
        elif lis[i] == 'S':
            s_index = i
            break

    function(b_index, s_index, lis)
    if not bool2:
        print('NO')
        return
    recursion(lis)

while True:
    x = input()
    if x == "X":
        break
    lis = list(x)
    s, b = lis.count('B'), lis.count('S')
    if s != b:
        print('NO')
    else:
        recursion(lis)
