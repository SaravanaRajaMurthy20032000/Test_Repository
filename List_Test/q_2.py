# Write a program that accepts a list from the user. Your program should reverse the content of the list and print it. 
# Do not use the reverse() method.

l = []
for i in range(5):
    s = int(input("enter the num: "))
    l.append(s)
print(f"Before reverse {l}")
print(f"This is After reverse {l[::-1]}")
