num_count = 0
consonants = "bcdfghjklmnpqrstvwxyz"
while num_count < 1:
    string = str(input())
    if len(string) > 4:
     if string == 'quit!':
         break
     else:
      if string[-3] in consonants and string[-2] == 'o' and string[-1] == 'r':
       new_string = string[:-1] + "u" + string[-1:]
       print(new_string)
      else:
       print(string)
    else:
        print(string)
