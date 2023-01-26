import random

name = input('Введите свое имя: ')

popitka = 3
count = 1



number_x = random.randint(1, 10)
while count <= 3:
    try:
        number = int(input(f'Угадайте число от 1 до 10. У вас {popitka} попытки. Введите число:  '))
    except ValueError:
        print('Oshibka, vvedite tolko tsifri')
        continue

    if number == number_x:
        print('Вы угадали!')
    elif number < number_x:
        print(f'Ошибка. Ваша первая попытка неверна. Подсказка: задуманное число больше {number}. Попробуйте еще раз! Введите число: ')   
    elif number > number_x:
        print(f'Ошибка. Ваша первая попытка неверна. Подсказка: задуманное число меньше {number}. Попробуйте еще раз! Введите число: ') 
    elif number < 0 or number > 10:
        print('Введите число от 1 до 10')
    
    else:
        print('Ошибка')  
    count += 1
    popitka -= 1
    
print(f'{name}, игра окончена')