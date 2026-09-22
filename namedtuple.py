from collections import namedtuple

Student = namedtuple("Student", ["id", "name"])

student = Student(101, "Ruchitha")

print(student.name)
print(student.id)
