# List to store student records
students = []

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    roll = input("Enter student roll number: ")

    student = {
        "name": name,
        "age": age,
        "roll": roll
    }

    students.append(student)
    print("Student added successfully!")


# Function to display all students
def display_students():
    if len(students) == 0:
        print("No students found.")
        return

    
    for s in students:
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Roll No:", s["roll"])
        print("---------------------")
        return


# Function to search student by roll number
def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Roll No:", s["roll"])

    print("Student not found!")


# Function to delete a student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main menu function
def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Program exited.")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
main()