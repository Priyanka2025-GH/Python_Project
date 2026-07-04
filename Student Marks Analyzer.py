# 1.Student Marks Analyzer

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")

    phy = int(input("Enter marks of Physics: "))
    chem = int(input("Enter marks of Chemistry: "))
    maths = int(input("Enter marks of Maths: "))

    students[name] = [phy, chem, maths]

print("\nAverage Marks of Each Student:")

for name in students:
    marks = students[name]
    average = int(marks[0] + marks[1] + marks[2]) / 3
    print(name, "=", average)

topper_name = ""
max_marks = 0

for name in students:

    marks = students[name]
    total = marks[0] + marks[1] + marks[2]

    if total > max_marks:
        max_marks = total
        topper_name = name

print("\nTopper =", topper_name,)
print("Total Marks =", max_marks)

sum_phy = 0
sum_chem = 0
sum_maths = 0

for name in students:
    marks = students[name]

    sum_phy = sum_phy + marks[0]
    sum_chem = sum_chem + marks[1]
    sum_maths = sum_maths + marks[2]

print("\nSubject-wise Average:")
print("Physics =", sum_phy / n)
print("Chemistry =", sum_chem / n)
print("Maths =", sum_maths / n)