student_data = {"Rahul": 85,"Roy": 92,"Shaurya": 78,"Rana": 95}

name = input("Enter the student's name: ")

if name in student_data:
    print(f"{name}'s marks: {student_data[name]}")
else:
    print("Student not found.")

