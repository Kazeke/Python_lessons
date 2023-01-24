
# x[0] + x[1]**2 + x[2]**3
# [ x for x in array]

# summa = x[0] + x[1]**2 + x[2]**3

array = [(1, 2, 3), (4,5, -10), (235, 1, -200)]
print([ array[x] for x in range(len(array))])
array.sort(key=lambda zed: sum([zed[x]**(x+1) for x in range(len(zed))]))
print(array)