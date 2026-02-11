print("Welcome to Student Result Processing System")
def get_student_details():
    student_name=input("Enter Student Name: ")
    student_id=input("Enter Student ID: ")
    return student_name,student_id
def get_marks():
    subject_1=int(input("Enter Subject1 Marks:" ))
    subject_2=int(input("Enter Subject2 Marks:" ))
    subject_3=int(input("Enter Subject3 Marks:" ))
    return subject_1,subject_2,subject_3
def calculate_total(subject_1,subject_2,subject_3):
    total=subject_1+subject_2+subject_3
    return total
def calculate_average(total):
    average=total/3
    return average
def determine_result(subject_1,subject_2,subject_3,average):
        if subject_1 < 35 or subject_2 < 35 or subject_3 < 35:
            result="FAIL"
        else:
            result="PASS"
        if average>=90:
            grade="A"
        elif average>=74:
            grade="B"
        elif average>=60:
            grade="C"
        else:
            grade="D"
        return result,grade
def main():
    while True:
        student_name,student_id=get_student_details()
        subject_1,subject_2,subject_3=get_marks()
        total=calculate_total(subject_1,subject_2,subject_3)
        average=calculate_average(total)
        result,grade=determine_result(subject_1,subject_2,subject_3,average)
        print("Student Name: ",student_name)
        print("Student ID: ",student_id)
        print("Total: ",total)
        print("Average: ",average)
        print("Result: ",result)
        print("Grade: ",grade)
        choice = input("Do you want to enter another student? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()