from collections import deque

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        c = a+b
        a = b
        b = c
        # a, b = b, a+b
    print()


def fib2(end_value:int):    # write Fibonacci series up to n
    """Return a list with Fibonacci series."""
    arr =[]
    a, b = 0, 1
    while a < end_value:
        arr.append(a)
        a, b = b, a+b
    
    
    return arr  



# f = fib
# # Now call the function we just defined:
# f(2000)
# f(10)
# f(5)


values = fib2(end_value=12)



def hello(*args,**kwargs):
    for d in args:
        print(d)
    
    for k,v in kwargs.items():
        print(k,v)
    

def hello_pos(*args):
    """
        affiche args
    """
    print(args)

def hello_kw(**kwargs):
    print(kwargs)


hello('toto',nom='Gaurat',prenom='Fred',age=45,job='Dev')

l = ["Fred","Gaurat",45]
d = {"name":"Gaurat","firstname":"Fred","age":"45"}
# *l => "Fred","Gaurat",45
print(*l)
print("print l",l)
print("print *l",*l) # => print("Fred","Gaurat",45)
print("Fred","Gaurat",45)
print(*l)
hello_pos(*l)
hello_kw(**d) # hello_kw(name="Fred",firstname="Gaurat",age=45)
hello_kw(name="Fred",firstname="Gaurat",age=45)


