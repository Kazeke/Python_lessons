# import mymodule as mym

# mym.hello()
# print(mym.fib(10))
# print(mym.funk(2,4,6))

# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка

# mylist = [1,2,3,'my','home',True]

# mylist.append('its')
# print(mylist)

# mylist[4] = 189
# print(mylist)

# ylist = [1,2,3,4,5]
# mylist.append(ylist)
# print(mylist)

# tup = (1,2,3,4,6,87,8)
# mylist[-1] = tup
# print(mylist)

# print(mylist[-1])

# mylist.remove(189)
# print(mylist)

# # mylist.count(1)
# print(mylist.count(1))


# stri = [0]*5
# print(stri)
# summ = 0
# summa = 0
# chet = 0
# for i in range(5):
#     massiv = int(input('Vvedite chislo: '))
#     stri.append(massiv)
#     summa = summa + massiv
#     if massiv%2 == 0:
#             chet+=1
#     if massiv < 0:
#         summ = summ + 1        
# print(summ)
# print(summa)
# print(chet)

# for i in range(1, 11):
#     x = [i * 3]
#     print(x, end='')

# x = list() # x = []
# for i in range(3, 31, 3):
#     x.append(i)
# print(x)

# x = [i for i in range(3, 31, 3)]
# print(x)

# numbers1 = []
# numbers2 = list()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers2 = list(numbers)
# print(numbers2)

# a = list('Hello!')
# print(a)

# numbers = [1, 2, 3, 4, 5]
# print(numbers[0]) # 1
# print(numbers[2]) # 3
# print(numbers[-3]) # 3

# numbers[0] = 125 # изменяем первый элемент списка
# print(numbers[0]) # 125

# numbers = list(range(10))
# print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = list(range(2, 10))
# print(numbers) # [2, 3, 4, 5, 6, 7, 8, 9]
# numbers = list(range(10, 2, -2))
# print(numbers) # [10, 8, 6, 4]

