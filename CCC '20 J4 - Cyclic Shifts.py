string = list(input())
cyclic_shift = list(input())
def function():
    for i in range(len(string)):
        string1 = string[i:(len(cyclic_shift))+i]
        for j in range(len(cyclic_shift)):
            if cyclic_shift == string1:
                print('yes')
                return
            string1.append(string1.pop(0))
    print('no')
    return
function()
