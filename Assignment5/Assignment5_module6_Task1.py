student_data = {"Alice": 85,"Bob": 92,"Charlie": 78,"Diana": 95}

name = input("Enter the student's name: ")

if name in student_data:
    print(f"{name}'s marks: {student_data[name]}")
else:
    print("Student not found.")
