# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

# Выведите первый и последний элемент списка.
# lst = [1, 2, 3, 4, 5]

# lst = [1, 2, 3, 4, 5]
# # print(lst[0])
# # print(lst[-1])
# print(f'Первый: {lst[0]}; последний: {lst[-1]}')

# Задание:
# Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# ]

# for i in numbers:
#     if i%2 == 0:
#         print(i)
#     elif i == 237:
#         break

# Поменяйте значения переменных местами.
# x = 5
# y = 10
# z = 12

# z = x
# x = y
# y = z

# x, y, z = z, y, x
# print(f'{x}, {y}, {z}')

# Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).
# print('I',  'like', 'Python', sep = '***')

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.

# like = int(input('Число1: '))
# like2 = int(input('Число2: '))
# like3 = int(input('Число3: '))


# print('Сумма: ', like + like2 + like3)

# a = int(input())
# a += int(input())
# a += int(input())
# print(a)

# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

# str1 = int(input('Vvedite tseloe chislo: '))
# print(str1 + 1)
# print(str1 - 1)

# a = int(input('Vvedite tseloe chislo: '))
# print('Следующее за числом', a, 'число:', a+1)
# print('Для числа', a, 'предыдущее число:', a-1)

# Напишите программу, которая считывает целое положительное число x 
# и выводит на экран последовательность чисел x, 2x, 3x, 4x, 5x, 
# разделённых тремя черточками.


# number = int(input('Vvedite x : '))
# print(number, 2*number, 3*number, 4*number, 5*number, sep = '-'*3)

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

# num = int(input('Vvedite col sant: '))
# print(num // 100)

# Напишите программу, в которой рассчитывается сумма 
# и произведение цифр положительного трёхзначного числа.

# num = int(input('Chislo:'))
# num1 = num//100
# print(num1)
# num2 = num % 100 // 10
# print(num2)
# num3 = num % 10
# print(num3)
# print(num1+num2+num3)
# print(num1*num2*num3)