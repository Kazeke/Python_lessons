class Student:
    """Common base class for all students"""

    stdCount = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.stdCount += 1

    @staticmethod
    def student_count():
        print("Total Students %i" % Student.stdCount)

    def display_student(self):
        print("Name : ", self.name, '', "Age: ", self.age, "Grade: ", self.grade)

    def exam(self, new_grade):
        self.grade = new_grade
    
Kazeke = Student('Kazeke', 36, 5)
print(Kazeke.age)
Kazeke.exam(77)
print(Kazeke.age)