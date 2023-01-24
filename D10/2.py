class Animal:
    pass

class Cat(Animal):
    LAPS = 4
    TAIL = ''

    def __init__(self, name, age=0):
        self.age = age
        self.sex = 0
        self.weight = 0
        self.name = ''
        self.bread = ''

    def __str__(self):
        return ''


    # def __new__(cls, *args, **kwargs):
    #     pass
class Point:
    def __init__(self, x: int, y, z):
        print('Create decard point')
    def __init__(self, length, alph):
        print('Create from polar system')

if __name__ == '__main':
    vasilii = Cat('Vasilii',age=15)
    chernish = Cat('Chernish')
    chernish.TAIL = 'DSDS'

    print(vasilii.age)
    print(chernish.TAIL)
    print(f"Cat's name is {chernish.name}")
    print(Cat)
    # print(Animal.)