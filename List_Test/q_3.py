# Find and display the largest number of a list without using built-in function max().

l = []
for i in range(5):
    n = int(input("enter the num: "))
    l.append(n)
print(l)
# print(max(l))
print(sorted(l))