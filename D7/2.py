result = 0

for i in range(1000):
    if i % 2 == 0 or i % 5 !=0:
        #print(i)
        continue
    result +=i  
    print(i) 
print(result)