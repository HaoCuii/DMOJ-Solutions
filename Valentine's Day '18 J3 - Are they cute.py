names = []
cuteness = []
for i in range(int(input())):
    x,y = (input().split(' '))
    names.append(x)
    cuteness.append(int(y))
sort = sorted(cuteness)
for i in range(len(names)):
    if cuteness[i] > sort[len(cuteness)//2]:
        print(names[i],'is cute! <3')
    else:
        print(names[i],'is not cute. </3')