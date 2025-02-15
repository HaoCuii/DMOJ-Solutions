weight = float(input())
height = float(input())
BMI = (weight/(height*height))
if BMI > 25:
    print('Overweight')
elif BMI < 18.5:
    print('Underweight')
else:
    #Was a spelling error. I spelled Normal Weight with a capitol and would have wasted a lot of my time if my code was more complex
    print('Normal weight')
