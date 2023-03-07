import random
list_with_numbers = list(range(10))

# new_list = []

# for i in list_with_numbers:
#     if not i%2: # i%2==0
#         print(i)
#         new_list.append(i + random.random())
# print(new_list)

new_list_2 = [i + random.random() for i in list_with_numbers if not i%2]
print(new_list_2)