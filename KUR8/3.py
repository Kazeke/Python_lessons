def fac(N):

    fact = 1
    for i in range(2,N+1):
        fact = fact * i 
    return fact

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)

print(fac(5))
print(factorial_recursive(4))