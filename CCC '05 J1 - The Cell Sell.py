day = int(input())
night = int(input())
weekend = int(input())

day_a = max((day-100)*25,0)
night_a = night*15
weekend_a = weekend*20
total = day_a + night_a + weekend_a
print('Plan A costs',"{:.2f}".format(total/100))

day_b = max((day-250)*45,0)
night_b = night*35
weekend_b = weekend*25
total2 = day_b + night_b + weekend_b
print('Plan B costs',"{:.2f}".format(total2/100))

if total > total2:
    print('Plan B is cheapest.')
elif total < total2:
    print('Plan A is cheapest.')
else:
    print('Plan A and B are the same price.')