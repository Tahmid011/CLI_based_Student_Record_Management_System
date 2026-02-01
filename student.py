class Student:
    def __init__(self, name, roll, email, department):
        self.name = name
        self.roll = roll
        self.email = email
        self.department = department

    def to_string(self):
        # Save student as one line in text file
        return f"{self.name}|{self.roll}|{self.email}|{self.department}"

    @staticmethod
    def from_string(line):
        name, roll, email, department = line.strip().split("|")
        return Student(name, int(roll), email, department)