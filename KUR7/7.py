# ЗАДАЧА 7
from collections import Counter

pasajiri = []
while True:
    print('Кто пересекает границу: ')
    imena = input()
    if imena == 'END':
        break
    pasajiri.append(imena)
cnt = Counter(pasajiri)
dict = dict(cnt)
for key in dict:
    print(key,'-',dict[key])