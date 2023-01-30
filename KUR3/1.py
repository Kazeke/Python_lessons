import random
# i = 0

# while i < 5:
#     print(i)
#     i += 1

# text = 'Hello world'

# u = 0
# while u < len(text):
#     print(text[u])
#     u += 1

# k = 0

# while True:
#     if k == 3:
#         break
#     print(k)
#     k += 1

# Вот еще один пример использования цикла while 
# для определения количества цифр натурального числа n


# number = int(input('vvedite chislo: '))

# len = 0 
# while number > 0:
#     number = number // 10 # number //=10   
#     print(number)
#     len += 1
# print(len)

# number = int(input('vvedite chislo: '))

# i = 1
# while i**2 < number:
#     print(i**2)
#     i += 1

# number = int(input('vvedite chislo: '))

# while number % 13 != 0: # 20 % 13 (7) != 0  26 % 13 (0) != 0 
#     print(number)
#     number += 1

# i = 1
# while True:
#     number = int(input('vvedite chislo: '))

#     if number == 0:
#         break
#     i = i * number
# print(i)

# i = 1
# while True:
#     number = int(input('vvedite chislo: '))

#     if number == 11:
#         break
#     i = i + number
# print(i - 1)

# number = int(input('vvedite chislo: '))
# i = 0
# while number!=0:
#     if number%2 == 0:
#         i += 1
#     number = int(input('vvedite chislo: '))
# print(i)

# a = 0
# b = -1
# n = 1
# while n:
#     n = int(input())
#     a = a + n
#     b = b + 1
# print(a/b)


# Напишите программу, 
# которая бы «Подбрасывала» условную монету 100 раз 
# и сообщала, сколько раз выпал орел, а сколько — решка.

# i = 0
# l = 0
# while i < 100:
#     k = random.randrange(2)
#     if k == 0:
#         l += 1
#     i += 1
# print('Orel:',l, 'Reshka:', 100-l)