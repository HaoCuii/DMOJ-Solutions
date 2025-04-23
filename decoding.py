def foo():
    x = 'asdf'
    y = 'asdf' + "asdf"
    def magic(n):
        print(f"Magic value: {n}")  # Could be any formatting!
    magic(y)

def bar(n):
    print(n)

def f(x): return 2*x
def reverse_fn(f): return lambda x, funct=f: funct(-x) 
print(reverse_fn(4)