class Animal:
    pass


class Cat(Animal):
    LAPS = 4
    TAIL = ""

    def __init__(self, name, age=0, *args, **kwargs):
        self.age = age
        self.sex = 0
        self.weight = 0
        self.name = name
        self.bread = ""
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f"This is cat {self.name}, {self.age} years old"
    # def __new__(cls, *args, **kwargs):
    #     pass


class Point:
    def __init__(self, x: int, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        print("Create decard point")


    def __str__(self):
        return f"Point {self.x} {self.y} {self.z}"

    @staticmethod
    def sum_two_point(point_one, point_two):
        return Point(
            point_one.x + point_two.x,
            point_one.y + point_two.y,
            point_one.z + point_two.z
            )


def create_cat():
    vas = ("Vas")
    return vas


if __name__ == '__main__':
    a = Point(1, 2, 3)
    b = Point(10, -10, 0)
    print(b.sum_two_point(a, b))
    print(b._Point__var)

    # vasilii = Cat("Vasilii", age=15)
    # chernish = Cat("Chernish")
    # chernish.TAIL = "dsds"
    # print(vasilii.age)
    # print(chernish.TAIL)
    # print(f"Cat's name is {chernish.name}")
    # print(vasilii)
    # print(12)
    # print(Animal.__mro__)
