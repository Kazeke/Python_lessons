# задание 6

import random 

sum = 0
max = 0
sum_1 = 0
min_2 = 10
max_gl_diag = 0

x = [[random.randint(0, 10) for i in range(4)] for j in range(3)]

for i in range(3):
    for j in range(4):

        print(x[i][j],end='\t') 
        # 1 заход     x[0][0], 2 -x[0][1], 3 - x[0][2], 4 x[0][3], 
        # 2 заход 5 - x[1][0], 6 - x[1][1], 7 - x[1][2], 8 - x[1][3]
        # 3 заход 5 - x[2][0], 6 - x[2][1], 7 - x[2][2], 8 - x[2][3]

        # считаем сумму
        sum = sum +x[i][j]

        # считаем мах элемент
        if x[i][j] > max:
            max = x[i][j]
        
        # считает сумму 1 строки
        if i == 0:
            sum_1 = sum_1 + x[i][j]

        # минимальный элемент во втором столбце
        if j == 1:
            if x[i][j] < min_2:
                min_2 = x[i][j]

        # максимальный элемент по диагонали
        if i == j:
            if x[i][j] > max_gl_diag:
                max_gl_diag = x[i][j]

    print()
print()
print('считаем сумму: ', sum)
print('считаем мах элемент: ', max)
print('считает сумму 1 строки: ', sum_1)
print('минимальный элемент во втором столбце: ', min_2)
print('максимальный элемент по диагонали: ', max_gl_diag)
