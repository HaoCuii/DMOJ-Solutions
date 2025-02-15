string = str(input())

happy = string.count(":-)")
sad = string.count(":-(")
if happy > sad:
 print("happy")
elif happy < sad:
 print('sad')
elif happy == sad and sad != 0:
 print('unsure')
else:
 print('none')
