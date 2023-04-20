# 3. Find the faculty with least pass percentage (<= 40%)
import csv

def fac_least_pass_percentage(student_marks,subject_faculty):
    Telugu = 0
    English = 0
    Maths = 0
    Physics = 0
    Chemistry = 0
    Social = 0

    least_mark = {}
    msg3 = None

    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for marks in data:
            if int(marks['Telugu']) <= 40:
                Telugu += 1
            if int(marks['English']) <= 40:
                English += 1
            if int(marks['Maths']) <= 40:
                Maths += 1
            if int(marks['Physics']) <= 40:
                Physics += 1
            if int(marks['Chemistry']) <= 40:
                Chemistry += 1
            if int(marks['Social']) <= 40:
                Social += 1
        
        least_mark = {
            'Telugu' : Telugu,
            'English' : English,
            'Mathematics' : Maths,
            'Physics' : Physics,
            'Chemistry' : Chemistry,
            'Social' : Social
        }

    least_pass_perc = max(least_mark.items(),key=lambda x:x[1])
    print(least_pass_perc)

    with open(subject_faculty,'r') as csvfile:
        faculty_data = list(csv.DictReader(csvfile))
        for i in faculty_data:
            if least_pass_perc[0] == i['Subject']:
                msg3 = f"The faculty with least pass percentage with less than or equal to 40% is {i['Faculty']} and his subject is {i['Subject']}."
    return msg3

print(fac_least_pass_percentage('function_assignments/student_marks.csv','function_assignments/subject_faculty.csv'))