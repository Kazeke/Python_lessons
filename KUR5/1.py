import math

# Написать функцию arithmetic, принимающую 3 аргумента: 
# первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
# Если третий аргумент +, сложить их; если —, то вычесть;
#  * — умножить; / — разделить (первое на второе). 
# В остальных случаях вернуть строку "Неизвестная операция ".

# def arithmetic(n1, n2, o):
#     if o == '+':
#         return n1 + n2
#     elif o == '-':
#         return n1 - n2
#     elif o == '*':
#         return n1 * n2
#     elif o == '/':
#         return n1/n2
#     else:
#         print('Neizvestnaya operatsia')
# print(arithmetic(4, 2, '/'))

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
# и возвращающую время года, которому этот месяц принадлежит 
# (зима, весна, лето или осень).

# def season(mes):
#     if mes == 12 or mes == 1 or mes == 2:
#         return 'zima'
#     elif mes == 3 or mes == 4 or mes == 5:
#         return 'vesna'
#     elif mes == 6 or mes == 7 or mes == 8:
#         return 'leto'
#     elif mes == 9 or mes == 10 or mes == 11:
#         return 'osen'
# print(season(10))

# Написать функцию square, принимающую 1 аргумент — сторону квадрата, 
# и возвращающую 3 значения: 
# периметр квадрата, площадь квадрата и диагональ квадрата.

# def square(a):
#     d = a * math.sqrt(2)
#     S = a * a         #math.pow(a, 2)
#     P = a * 4
#     return d, S, P
# print(square(3))

# Пользователь делает вклад в размере a рублей 
# сроком на years лет под 10% годовых (каждый год размер его вклада 
# увеличивается на 10%. Эти деньги прибавляются к сумме вклада, 
# и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, 
# и возвращающую сумму, которая будет на счету пользователя.

# def bank(a, years):
#     deposit = a
#     coifitsient = 1.1 # deposit + deposit*0.1
#     year = 1
#     while year <= years:
#         deposit = deposit * coifitsient
#         year +=1
#     return deposit
# print(bank(100, 3))

# def bank(a, years):
#     for year in range(years):
#         a*=1.1 # a = a * 1.1
#         print(a)
#         print('------------------------')
#     return a
# print(bank(100, 3))

# a = float(input('vvedite chislo: '))

# def F(X,Y):
#     return (X + Y)/(math.pow(X, 2) -1)
# print(F(4,12)-F(2*a,8))

# t = float(input('vvedite chislo1: '))
# s = float(input('vvedite chislo2: '))

# def f(a,b,c):
#     return (2*a - b - math.sin(c))/(5 + math.fabs(c))
# print(f(t, -2*s, 1.17)+f(2.2,t,s-t))

