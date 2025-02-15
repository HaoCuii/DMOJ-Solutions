pepers = {'Poblano':1500,
          'Mirasol':6000,
          'Serrano':15500,
          'Cayenne':40000,
          'Thai':75000,
          'Habanero':125000,}
x = int(input())
spice = 0
for i in range(x):
    z = input()
    spice += pepers[z]
print(spice)