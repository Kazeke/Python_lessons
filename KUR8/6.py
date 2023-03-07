nums = [(1,1,1), (1,2,3), (-1,-1,7), (-3,-2,8), (0,0,0), (3,-4,-5)]

# сортировка по сумме кортежей
print(sorted(nums, key=sum))

# сортировка по третьим элементам
print(sorted(nums, key=lambda tup: tup[2]))

nams = {'b':3, 'c':2, 'a':4, 'd': 1}

# ключи в алфавитном порядке
print(sorted(nams))

print(sorted(nams.items(), key=lambda item: item[1], reverse=True))
#print(sorted(nams.items(), reverse=True))