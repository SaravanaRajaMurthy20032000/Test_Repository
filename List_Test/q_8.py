# Write a program that accepts a list from the user and print the list after removing all elements which are divided by 3.

l = []
for i in range(5):
    n = int(input("user input: "))
    if n % 3 == 0:
        print("true")
    else:
        print("false")
    l.append(n)
print(l)
