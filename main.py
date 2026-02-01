from manager import StudentManager


def show_menu():
    print("\n=========== MENU ===========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    print("============================")


def main():
    print("Welcome to the Student Record Management System!\n")
    print("Loading student records from students.txt... Done!")

    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.remove_student()
        elif choice == "5":
            print("Thank you for using the Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
