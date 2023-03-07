import math 

def hello():
    print('Hello, world!')

def fib(x):
    b=2*x+5
    return b

def funk(x,y,z):
    S = math.sqrt(math.pow(x,2)+ math.pow(y,2) + math.pow(math.sin(x*y), 2) + math.sqrt(math.pow(y,2) + z**2 + math.sin(y*z)**2 + math.sqrt(z**2 + y**2 + math.sin(z*x)**2) ))
    return S
