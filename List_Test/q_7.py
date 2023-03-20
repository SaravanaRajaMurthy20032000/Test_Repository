# Write a program that accepts a list from the user and check whether your list is having any element or empty.
l=[]
for i in range(2):
    n = (input("user input: "))
    l.append(n)
    if n in l:
        print("not empty")
    elif n not in l: # its wrong
        print("empty") 
print(l)