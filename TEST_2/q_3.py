students = [
 	("John", ["Computers", "Physics", "Maths"]), 
	("Wasim", ["Maths", "Computers", "Statistics"]), 
	("Naresh", ["Computers", "Accounting", "Economics"]), 
	("SaiTeja", ["English", "Accounting", "Economics", "Law"]), 
	("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])
]
c = 0
for student in students:
    if "Computers" in student[1]:
        c += 1
print(c)