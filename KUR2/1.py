import math
# При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.
# Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

# password1 = input('Vvedite parol1: ')
# password2 = input('Vvedite parol2: ')
# if password1 == password2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# Напишите программу, которая определяет, является число четным или нечетным.

# password = int(input('Vvedite chislo: '))

# if password %2 == 0:
#     print('Chetnoe')
# elif password == 0:
#     print('eto nol')
# else:
#     print('Nechetnoe')

# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
# Формат входных данных
# На вход программе подаётся целое число — возраст пользователя.
# Формат выходных данных
# Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.

# vosrast = int(input('Vvedite vosrast: '))

# if vosrast >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# Составить программу, которая вычислит значение:
# chislo = int(input('Vvedite chislo: '))
# if chislo == 5 or chislo == 8:
#     print('y =', math.exp(chislo)) #y = e**chislo
# elif chislo == 9 or chislo == 10:
#     print('y = ', 6 * chislo + 8)
# elif chislo == 0:
#     print('y = 10')
# elif chislo < 0:
#     print('y = 13')
# else:
#     print('error')

# Напишите программу, которая принимает три положительных 
# числа и определяет вид треугольника, 
# длины сторон которого равны введенным числам.

# chislo1 = int(input('Vvedite chislo: '))
# chislo2 = int(input('Vvedite chislo: '))
# chislo3 = int(input('Vvedite chislo: '))

# if chislo1 == chislo2 == chislo3:
#     print('ravnomernii')
# elif chislo1 == chislo2 or chislo2 == chislo3 or chislo1 == chislo3:
#     print('ravnobedrenni')
# else:
#     print('rasnostoronnii')

# Составить программу для вычисления площади круга.

# radius = int(input('Vvedite radius: '))
# s = math.pi * math.pow(radius, 2) # radius **2
# print(s)

# Составить программу, которая будет выводить значение True, 
# если указанное высказывание является истинным, и False в противном случае:

# znach = int(input('Vvedite znach: '))
# if znach %2 == 1: # !=0
#     print(True)
# if znach %2 == 0:
#     print(False)

# for i in range(15, 9, -1):
#     print(i)

# i = 15
# while i > 10:
#     print(i)
#     i -= 1

# x = 32
# while x >= 20:
#     print(x)
#     x -= 2

# x = 50
# while x <= 100:
#     print(x)
#     x += 10

# x = 31
# while x <= 60:
#     print(x)
#     x += 2

# x = 32
# while x >= 20:
#     print(x)
#     x -= 2

# x = 1
# y = 0 
# while x <= 5:
#     chislo = float(input('Vvedite chislo: '))
#     if chislo < 0:
#         y += 1
#     x += 1
# print(y)