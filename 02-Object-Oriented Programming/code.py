class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades)
print(Student.average(student))
print(student.average())


"""
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))
print(student.average())

"""


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (89, 90, 93, 78, 90))
print(student.name)
print(student.average_grade())