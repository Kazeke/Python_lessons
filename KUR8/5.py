import string

sentence = 'I am@Python@senior^pomidor'

list_with_words = sentence.split()
new_list = []

for word in list_with_words:
    if not word in string.punctuation:
        new_list.append(word)

print(new_list)

new_list2 = [word for word in list_with_words if not word in string.punctuation ]
print(new_list2)