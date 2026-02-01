import os
from student import Student

FILE_NAME = "students.txt"


class Storage:
    def load(self):
        students = []
        if not os.path.exists(FILE_NAME):
            return students

        file = open(FILE_NAME, "r")
        for line in file:
            if line.strip() != "":
                students.append(Student.from_string(line))
        file.close()
        return students

    def save(self, students):
        file = open(FILE_NAME, "w")
        for s in students:
            file.write(s.to_string() + "\n")
        file.close()
