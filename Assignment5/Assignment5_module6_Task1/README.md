# tutedude_python_assignments: Assignment5_module6_Task1
student_data = {"Rahul": 85,"Roy": 92,"Shaurya": 78,"Rana": 95}

name = input("Enter the student's name: ")

if name in student_data:
    print(f"{name}'s marks: {student_data[name]}")
else:
    print("Student not found.")


# tutedude_python_assignments: Assignment5_module6_Task2
Number=[1,2,3,4,5,6,7,8,9,10]
#print(type(Number))
print(f'Original list:{Number}')
order=Number[0:5:1]
print(f'Extracted first five elements:{order}')
reversed_number=order[::-1]
print(f'Reversed extracted elements:{reversed_number}')
