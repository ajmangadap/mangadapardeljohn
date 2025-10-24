# student_grades.py

students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input(f"Enter {name}'s grade: "))
    students.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}")

def display_students():
    print("\nStudent Grades:")
    if not students:
        print("No students added yet.")
    else:
        for i in range(len(students)):
            print(f"{students[i]}: {grades[i]}")

def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"\nAverage Grade: {avg:.1f}")
    else:
        print("No grades entered.")

def highest_grade():
    if grades:
        print(f"Highest Grade: {max(grades)}")
    else:
        print("No grades entered.")

def list_operations():
    numbers = [5, 2, 8, 1, 9, 3]
    print("\nOriginal List:", numbers)
    numbers.sort()
    print("Sorted List:", numbers)
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers)/len(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Length:", len(numbers))

# Main menu
while True:
    print("\n=== MAIN MENU ===")
    print("1. Student Grade Manager")
    print("2. List Operations Practice")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            print("\n--- Student Grade Manager ---")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Show Average Grade")
            print("4. Show Highest Grade")
            print("0. Back to Main Menu")

            sub_choice = input("Choose an option: ")

            if sub_choice == "1":
                add_student()
            elif sub_choice == "2":
                display_students()
            elif sub_choice == "3":
                average_grade()
            elif sub_choice == "4":
                highest_grade()
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice, try again.")

    elif choice == "2":
        list_operations()

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
