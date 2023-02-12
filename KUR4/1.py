import math

# Объявление функции
# def hello(name):
#     print('Hello, ' + name)

# Вызовы функции
# hello('Max')
# hello('Ivan')
# hello('Alex')
# hello('Kate')

# def sum(number1, number2):
#     summa= number1 + number2
#     print('Summa: ', summa)
# sum(1, 2)

# def sum(number1, number2):
#     return number1 + number2
# b = sum(1, 2)
# print(b)
# Вызовы функции

# s1 = sum(10, 2)
# s2 = sum(108, 100)
# s3 = sum(3, 1)

# print(f's1 = {s1}')
# print(f's2 = {s2}')
# print(f's3 = {s3}')

# def sum(n1, n2):
#     return n1 * n2
# s = sum(2, 3)
# print(s)

# def sum(n1):
#     return n1 * n1
# s = sum(6)
# print(s)

# Напишите функцию isEven, возвращающую True, 
# если число четное, и False, если - нечетное

# def isEven(n1):
#     return n1%2 == 0

# s = isEven(7)
# print(s)
# v = isEven(6)
# print(v)

# def circle(n1):
#     return math.pi * n1*n1
# print(circle(4))

# def numb(s1):
#     return s1%3==0
# print(numb(5))

# def numb(s1):
#     if s1 > 0 and s1%2==0:
#         return True
#     else:
#         return False
# print(numb(-5))

# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))

# def sum(n1, n2):
#     if n1 < n2:
#         return n2
#     return n1
# print(sum(400,700))

# def sum1(n1, n2, n3):
#     return sum(n1,sum(n2, n3))
# print(sum1(1,2,3))

# def square(s1, s2):
#     sq = (s1 + s2**2)/s1
#     return sq


# S1 = float(input('Введите площадь первого прямоугольника: '))
# S2 = float(input('Введите площадь второго прямоугольника: '))

# S = square(S1, S2)
# print('S =', S)

# def pip(p1, p2):
#     pipi = (math.sqrt(p1) - p2)/(p1 + p2)
#     return pipi

# P1 = float(input('chislo1: '))
# P2 = float(input('chislo2: '))

# w = pip(P1, P2)
# print(w)

# def step(n1,n2,n3):
#     ste = n1**5 + n2**7 + n3**4
#     return ste

# X = int(input('chislo1: '))
# Y = int(input('chislo2: '))
# Z = int(input('chislo3: '))

# print(step(X, Y, Z))

# def sqe(a, b):
#     squre = a * b
#     perim = (a + b)*2
#     return squre, perim

# X = float(input('chislo1: '))
# Y = float(input('chislo2: '))
# print(sqe(X, Y))

n = int(input())
 
suma = 0
mult = 1
 
while n > 0:
    digit = n % 10 # 5    / 2 
    suma = suma + digit # 0 + 5 = 5  /7
    mult = mult * digit # 0 * 5 = 5  10
    n = n // 10 # 2
 
print("Сумма:", suma)
print("Произведение:", mult)

