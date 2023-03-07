# 08.02.23 - 2 урок

# li = [1,2,3,4,5]
# for i in li:
#     print(i)

# pr = input('Vvedite: ').split()
# for i in range(0, len(pr), 2):
#         print(pr[i])

# pr = input('Vvedite: ')
# li = [int(pr) for pr in pr.split()]

# for i in li:
#     if i %2 == 0:
#         print(i)

# pr = input('Vvedite: ')
# li = [int(pr) for pr in pr.split()]

# kol = 0
# for i in li:
#     if i > 0:
#         kol +=1
# print(kol)

li = input('Vvedite: ').split()

kol = 0
for i in range(1, len(li)):
    if int(li[i-1]) < int(li[i]) and int(li[i]) < int(li[i+1]):          
        kol +=1
print(kol)

