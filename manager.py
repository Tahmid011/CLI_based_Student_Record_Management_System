from student import Student
from storage import Storage


class StudentManager:
    def __init__(self):
        self.storage = Storage()
        self.students = self.storage.load()

    def add_student(self):
        name = input("Enter Student Name: ").strip()
        if name == "":
            print("Error: Name cannot be empty")
            return

        roll_input = input("Enter Roll Number: ").strip()
        if not roll_input.isdigit():
            print("Error: Roll number must be an integer")
            return
        roll = int(roll_input)

        # Check duplicate roll
        for s in self.students:
            if s.roll == roll:
                print("Error: Roll number already exists for another student.")
                return

        email = input("Enter Email: ").strip()
        if email == "":
            print("Error: Email cannot be empty")
            return

        department = input("Enter Department: ").strip()
        if department == "":
            print("Error: Department cannot be empty")
            return

        self.students.append(Student(name, roll, email, department))
        self.storage.save(self.students)
        print("Student record added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        print("\n===== All Students =====")
        count = 1
        for s in self.students:
            print(f"{count}. Name : {s.name}")
            print(f"   Roll : {s.roll}")
            print(f"   Email : {s.email}")
            print(f"   Department : {s.department}\n")
            count += 1
        print("========================")

    def search_student(self):
        term = input("Enter search term (name/email/roll): ").strip().lower()
        found = False

        for s in self.students:
            if term in s.name.lower() or term in s.email.lower() or term == str(s.roll):
                if not found:
                    print("\nSearch Result:\n")
                found = True
                print(f"Name : {s.name}")
                print(f"Roll : {s.roll}")
                print(f"Email : {s.email}")
                print(f"Department : {s.department}\n")

        if not found:
            print("No matching student found.")

    def remove_student(self):
        roll_input = input("Enter the roll number of the student to delete: ").strip()
        if not roll_input.isdigit():
            print("Error: Roll number must be an integer")
            return
        roll = int(roll_input)

        for s in self.students:
            if s.roll == roll:
                confirm = input(f"Are you sure you want to delete student with roll number {roll}? (y/n): ").lower()
                if confirm == "y":
                    self.students.remove(s)
                    self.storage.save(self.students)
                    print("Student record deleted successfully!")
                else:
                    print("Deletion cancelled.")
                return

        print("Error: No student found with that roll number.")