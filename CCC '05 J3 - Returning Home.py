inputs = []
num = -1
count = 0
while True:
 user_input = str(input())
 if user_input == 'SCHOOL':
  break
 else:
  inputs.append(user_input)


inputs.insert(0, 'HOME.')


for index, i in enumerate(inputs):
 if inputs[num] == 'R': #FIRST ONE
  new_num = len(inputs) - ((len(inputs)/2) - 1)
  if index == len(inputs) - new_num:  
   num -= 1
   print('Turn LEFT into your ' + inputs[num])
   break
  num -= 1
  print('Turn LEFT onto ' + inputs[num] + ' street.')
  num -= 1


 elif inputs[num] == 'L':  #SECOND ONE
  new_num = len(inputs) - ((len(inputs)/2) - 1)
  if index == len(inputs) - new_num:  
   num -= 1
   print('Turn RIGHT into your ' + inputs[num])
   break
  num -= 1
  print('Turn RIGHT onto ' + inputs[num] + ' street.')
  num -= 1
  