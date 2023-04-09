# 1. Find the faculty with highest student count who got more than 90%.
import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

sub_faculty = {
    'Maths' : 'Murali Krishna',
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Social' : 'Krishna Reddy',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi'}

high_marks = {}

with open('E:/Test_Repo/Test_Repository/Assignments/student_marks.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    for records in data:
        if int(records['Telugu']) >= 90:
            Telugu += 1
        if int(records['English']) >= 90:
            English += 1
        if int(records['Maths']) >= 90:
            Maths += 1
        if int(records['Physics']) >= 90:
            Physics += 1
        if int(records['Chemistry']) >= 90:
            Chemistry += 1
        if int(records['Social']) >= 90:
            Social += 1

    high_marks['Telugu'] = Telugu
    high_marks['English'] = English
    high_marks['Maths'] = Maths
    high_marks['Physics'] = Physics
    high_marks['Chemistry'] = Chemistry
    high_marks['Social'] = Social

max_marks = max(high_marks.items(),key = lambda x: x[1])
faculty = (max_marks); (sub,marks) = faculty
print(f"The faculty with highest student count who got more than 90% is {sub_faculty[sub]} and his subject is {sub} with marks as {marks}")
