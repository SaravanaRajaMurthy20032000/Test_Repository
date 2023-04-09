num = input("enter the num: ")
count = 0
for i in num:
    if i.isdigit():
        count += 1
print(f"The number of digits in given number is {count}")
