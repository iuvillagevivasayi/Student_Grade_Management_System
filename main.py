import os

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data storage
students = []

# Add a new student
def add_student():
    name = input("Enter student's name: ")
    roll_no = input("Enter roll number: ")
    grades = input("Enter grades separated by spaces (e.g., 85 90 78): ")
    grades = list(map(int, grades.split()))
    students.append({
        'name': name,
        'roll_no': roll_no,
        'grades': grades
    })
    print("Student added successfully!")

# Display all students
def display_students():
    if not students:
        print("No student records found.")
        return
    for idx, student in enumerate(students, 1):
        print(f"\nStudent {idx}")
        print(f"Name: {student['name']}")
        print(f"Roll No: {student['roll_no']}")
        print(f"Grades: {student['grades']}")
        print(f"Average Grade: {sum(student['grades']) / len(student['grades']):.2f}")

# Save data to file
def save_to_file():
    with open("students_data.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['roll_no']},{' '.join(map(str, student['grades']))}\n")
    print("Data saved to 'students_data.txt'!")

# Load data from file
def load_from_file():
    try:
        with open("students_data.txt", "r") as file:
            for line in file:
                name, roll_no, grades = line.strip().split(",")
                grades = list(map(int, grades.split()))
                students.append({'name': name, 'roll_no': roll_no, 'grades': grades})
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found!")

# Main menu
def main():
    while True:
        clear_console()
        print("=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            save_to_file()
        elif choice == '4':
            load_from_file()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        input("\nPress Enter to continue...")

# Run the application
if __name__ == "__main__":
    main()


