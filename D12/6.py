import os

name_dir = 'D12'
file = 'file.txt'
path_to_file = os.path.join(name_dir, file)

try:
    with open(path_to_file,"a+") as f:
        some_list = ['привет \n', 'мир \n', 'hello\n']
        f.writelines(some_list)
        # f.write('I LOVE PYTHON')
        # print(f.read(4))
        # print(f.read(4))
        # print(f.read(4))
        # print(f.read(4))

        #stuff goes here
except IOError:
    pass
    #do what you want if there is an error with the file opening