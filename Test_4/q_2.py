digit_number = int(input("enter the num: "))
if digit_number < 10:
    print(f"This {digit_number} is Single digit number")
elif digit_number < 100:
    print(f"This {digit_number} is Double digit number")
else :
    print(f"This {digit_number} is Big digit number")