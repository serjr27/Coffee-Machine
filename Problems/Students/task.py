class Student:
    all_students = []

    def __init__(self, name, last_name, birth_year: str):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year
        Student.all_students.append(self)


student = Student(input(), input(), input())
print(student.id)
