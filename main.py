def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

grade = calculate_grade(marks)

print("\n--- Student Result ---")
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Thank you for using Student Grade Calculator!")
