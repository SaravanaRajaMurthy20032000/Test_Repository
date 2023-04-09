# Write a program "num_identifier.py" that will print whether the number is a single digit number or double digit number or big number.
# If given number is one digit number, print "Single digit number"
# If given number is two digit number, print "Double digit number"
# If number is three digit number or bigger, print "Big number"

digit_number = int(input("enter the num: "))
if digit_number < 10:
    print(f"This {digit_number} is Single digit number")
elif digit_number < 100:
    print(f"This {digit_number} is Double digit number")
else :
    print(f"This {digit_number} is Big digit number")