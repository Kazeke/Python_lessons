matrix = np.array([[randint(0, 10) for i in range(3)] for x in range(3)])
print('Матрица - \n', matrix, '\n')

print('Сумма всех чисел в матрице: ', sum(map(sum, matrix)))
print('Максимальный элемент в матрице: ', max(map(max, matrix)))
print('Сумма чисел в первой строке: ', sum(matrix[0]))

result = []

for i in matrix:
    result.append(i[1])

print('Минимальный элемент во втором столбце: ', min(result))

max_num = 0
count = 0
result2 = []

for i in matrix:
    result2.append(i[count])
    count += 1

print('Максимальный элемент по главной диагонали', max(result2))


# import math

# x = [0,1,2,3,4,5,6,7,8,9]
# print(x[0], x[1], x[2])
# print(x[3], x[4], x[5])
# print(x[6], x[7], x[8])
# print(x[9])


# print('Сумма всех чисел: ', x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9])
# print('Максимальный элемент: ', max(x))
# print('Сумма чисел в первой строке: ', x[0] + x[1] + x[2])
