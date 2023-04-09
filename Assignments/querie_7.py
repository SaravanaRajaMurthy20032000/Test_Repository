# 7. Find the student with least numbers of marks as total.
import csv

with open('E:/Test_Repo/Test_Repository/Assignments/student_marks.csv') as csvfile:
    data = csv.DictReader(csvfile)
    total_marks = {}
    for records in data:
        marks = (int(records['Telugu']), int(records['English']), int(records['Maths']), int(records['Physics']), 
                 int(records['Chemistry']), int(records['Social']))
        total = sum(marks)
        total_marks[records['studentname']] = total
    students = sorted(total_marks.items(), key=lambda x: x[1])
print(f"The Student is {students[0][0]} and his Least mark is {students[0][1]}")
# print(students)