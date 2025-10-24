# student_records.py
import pickle

students = []

# === Student Record Functions ===
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students.append({"id": student_id, "name": name, "grade": grade})
    print(f"Added {name}")

def save_records(filename):
    with open(filename, 'wb') as f:
        pickle.dump(students, f)
    print("Records saved successfully!")

def load_records(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            print("\n--- Loaded Records ---")
            for s in data:
                print(f"ID: {s['id']} | Name: {s['name']} | Grade: {s['grade']}")
    except FileNotFoundError:
        print("File not found! Please save records first.")

def export_to_text(filename):
    if not students:
        print("No student data to export.")
        return
    with open(filename, 'w') as f:
        for s in students:
            f.write(f"{s['id']} - {s['name']} - {s['grade']}\n")
    print("Exported to text file successfully!")

# === File Operation Practice Function ===
def file_operations():
    try:
        with open("sample.txt", "w") as f:
            f.write("This is a new file.\n")
        with open("sample.txt", "a") as f:
            f.write("Appending more data.\n")
        with open("sample.txt", "r") as f:
            print("\n--- File Contents ---\n")
            print(f.read())
    except FileNotFoundError:
        print("File not found!")

# === MAIN MENU ===
while True:
    print("\n=== MAIN MENU ===")
    print("1. Student Records File System")
    print("2. File Operations Practice")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Submenu for Student Records
        while True:
            print("\n--- STUDENT RECORDS FILE SYSTEM ---")
            print("1. Add Student")
            print("2. Save to Pickle File")
            print("3. Load from Pickle File")
            print("4. Export to Text File")
            print("0. Back to Main Menu")

            sub_choice = input("Enter choice: ")

            if sub_choice == "1":
                add_student()
            elif sub_choice == "2":
                save_records("students.pkl")
            elif sub_choice == "3":
                load_records("students.pkl")
            elif sub_choice == "4":
                export_to_text("students.txt")
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice, try again.")

    elif choice == "2":
        file_operations()

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
