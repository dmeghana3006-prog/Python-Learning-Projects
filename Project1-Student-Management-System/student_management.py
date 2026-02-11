def add_student(students):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    student_marks = int(input("Enter Student Marks: "))

    students[student_id] = {
        "name": student_name,
        "marks": student_marks
    }
    print("Student added successfully!")
def view_students(students):
    if not students:
        print("No students found.")
    else:
        for student_id, info in students.items():
            print("ID:", student_id,
                  "| Name:", info["name"],
                  "| Marks:", info["marks"])
def search_student(students):
    checking = input("Enter Student ID: ")
    if checking in students:
        print("Name:", students[checking]["name"],
              "| Marks:", students[checking]["marks"])
    else:
        print("Student not found")
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    if student_id in students:
        new_name = input("Enter new name: ")
        new_marks = int(input("Enter new marks: "))

        students[student_id]["name"] = new_name
        students[student_id]["marks"] = new_marks

        print("Student updated successfully!")
    else:
        print("Student not found.")
def delete_student(students):
    student_id=input("Enter Student ID to delete: ")
    if student_id in students:
        students.pop(student_id)
    else:
        print("Student not Found")

def main():
    students = {}
    print("Welcome to Student Management System")
    while True:
        print("\n1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        option = int(input("Choose Your Option: "))

        if option == 1:
            add_student(students)
        elif option == 2:
            view_students(students)
        elif option == 3:
            search_student(students)
        elif option == 4:
            update_student(students)
        elif option==5:
            delete_student(students)
        elif option == 6:
            print("Thank you! Exiting the system.")
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    main()
