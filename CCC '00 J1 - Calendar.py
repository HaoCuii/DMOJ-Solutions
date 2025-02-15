input = str(input())
start,end = input.split()
start = int(start)
end = int(end)
num = list(range(1, end+1))
print('Sun Mon Tue Wed Thr Fri Sat')
line1 = [' ',' ',' ',' ',' ',' ',' ']
line2 = ['','','','','','','']
line3 = ['','','','','','','']
line4 = ['','','','','','','']
line5 = ['','','','','','','']
line6 = ['','','','','','','']
#line 1
counter = 0
num_count = 0
sml_start = start-1
for i in line1:
 if counter < (sml_start):
  line1[counter] = ''
  counter += 1
 else:
  line1[counter] = str(num[num_count])
  counter += 1
  num_count += 1

none = '  '

c = 0
for i in line1:
 if line1[c] == '':
     c += 1
     none += ' '
 else:
     c = 0
     break
fa = 0

#line 2
for i in line2:
  fs = str(num[num_count])
  if len(fs) == 1:
   if fa == 0:
    fs = '  ' + str(num[num_count])
    fa += 1
   else:
    fs = '   ' + str(num[num_count])
  else:
   fs = '  ' + str(num[num_count])
  line2[c] = fs
  c += 1
  num_count += 1

#line 3
fb = 0
d = 0
for i in line3:
  if d == 0:
   fs = str(num[num_count])
   if len(fs) == 1:
    fs = '  ' + str(num[num_count])
   else:
    fs = ' ' + str(num[num_count])
  else:
   fs = '  ' + str(num[num_count])
  line3[d] = fs
  d += 1
  num_count += 1

#line 4
fc = 0
h = 0
for i in line4:
  if h == 0:
   fc = str(num[num_count])
   if len(fs) == 1:
    fc = '  ' + str(num[num_count])
   else:
    fc = ' ' + str(num[num_count])
  else:
   fc = '  ' + str(num[num_count])
  line4[h] = fc
  h += 1
  num_count += 1

line11 = none+'   '.join(line1)
line22 = ''.join(line2)
line33 = ''.join(line3)
line44 = ''.join(line4)
print(line11)
print(line22)
print(line33)
print(line44)
if num_count != end:
 fg = 0
 j = 0
 for i in range(len(line5)):
  if num_count < end:
    if j < 7:
     fg = str(num[num_count])
     if j == 0:
      fg = ' ' + str(num[num_count])
      line5[j] = fg
      j += 1
      num_count += 1
     else:
      fg = '  ' + str(num[num_count])
      line5[j] = fg
      j += 1
      num_count += 1
    

 line55 = ''.join(line5)
 print(line55)
 
#line 6
if num_count!= end:
 fk = 0
 n = 0
 for i in range(len(line6)):
  if num_count < end:
    if n < 7:
     fk = str(num[num_count])
     if n == 0:
      fk = ' ' + str(num[num_count])
      line6[n] = fk
      n += 1
      num_count += 1
     else:
      fk = '  ' + str(num[num_count])
      line6[n] = fk
      n += 1
      num_count += 1
    

 line66 = ''.join(line6)
 print(line66)
