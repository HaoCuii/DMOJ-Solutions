t = int(input())
equation = []

for i in range(t):
    c_str, p_str = input().split()
    c = float(c_str)
    p = int(p_str)
    equation.append((c,p))
def derivative(function):
    f_prime = []
    for (c,p) in function:
        term = (0,1)
        if p != 0:
            term = ((c * p), p-1)
        f_prime.append(term)

    return f_prime
    
def apply_function(function,x):
    result = 0
    for (c,p) in function:
        result += c*(x**p)
    return result


def newton(estimate,iteration):
    if iteration == 500:
        return estimate
    d = derivative(equation)
    d = apply_function(d,estimate)
    f = apply_function(equation,estimate)
    next_estimate = estimate - (f/d)
    return newton(next_estimate,iteration+1)

s = set()
for i in range(-101,100,10):
    s.add(round(newton(i,1),7))

s = sorted(s)
real_roots = True
for i in s:
    if round(apply_function(equation,i),5) != 0:
        real_roots = False

if real_roots:
    for i in s:
        print(round(i,5))
else:
    print('NO REAL ROOTS')




