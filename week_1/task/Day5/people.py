class Person:
    name = ''
    age = 0
    department = ''

class Student(Person):
    id = 0
    GPA = 0.0
    advisor = Professor()

    def __init__(self, name, age, department, id, GPA):
        self.name = name
        self.age = age
        self.department = department
