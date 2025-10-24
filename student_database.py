# student_database.py

students = {}

# === Student Database Functions ===
def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exists!")
        return
    name = input("Enter name: ")
    grade = input("Enter grade: ")
    major = input("Enter major: ")
    students[student_id] = {'name': name, 'grade': grade, 'major': major}
    print(f"Added {name} (ID: {student_id})")

def get_student():
    student_id = input("Enter student ID to retrieve: ")
    info = students.get(student_id)
    if info:
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Grade: {info['grade']}")
        print(f"Major: {info['major']}")
    else:
        print("Student not found!")

def update_grade():
    student_id = input("Enter student ID to update grade: ")
    if student_id in students:
        new_grade = input("Enter new grade: ")
        students[student_id]['grade'] = new_grade
        print(f"Grade updated for {students[student_id]['name']}!")
    else:
        print("Student not found!")

def display_students():
    if not students:
        print("\nNo students in the database yet.")
        return
    print("\n--- All Students ---")
    for sid, info in students.items():
        print(f"{sid}: {info}")

# === Word Frequency Counter Function ===
def word_frequency_counter():
    print("\n--- Word Frequency Counter ---")
    text = input("Enter a short paragraph (2–3 sentences): ").lower()
    words = text.replace(".", "").split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("\n--- Word Frequencies ---")
    for word, count in sorted_words:
        print(f"{word}: {count}")
    print("Most common word:", sorted_words[0][0])

# === Main Menu ===
while True:
    print("\n=== MAIN MENU ===")
    print("1. Student Database")
    print("2. Word Frequency Counter")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Student Database Submenu
        while True:
            print("\n--- STUDENT DATABASE ---")
            print("1. Add Student")
            print("2. Get Student Info")
            print("3. Update Grade")
            print("4. Display All Students")
            print("0. Back to Main Menu")
            
            sub_choice = input("Enter choice: ")

            if sub_choice == "1":
                add_student()
            elif sub_choice == "2":
                get_student()
            elif sub_choice == "3":
                update_grade()
            elif sub_choice == "4":
                display_students()
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice, try again.")

    elif choice == "2":
        word_frequency_counter()

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
