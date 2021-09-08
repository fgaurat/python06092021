# import pckfib.fibo 
# import fibo
from pckfib import fibo
from pckfib.fibo import fib,fib2
# from fibo import *
from fibo import fib ,fib2 # as f
from pprint import pprint

def main(value=10):
    # fi.fib(value)
    fibo.fib(value)
    print(fibo.fib2(value))

if __name__ == '__main__':
    import sys
    value = int(sys.argv[-1])
    main(value)

