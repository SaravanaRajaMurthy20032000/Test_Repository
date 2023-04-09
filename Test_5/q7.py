# Define a function “sign” which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

def sign(num):
    if num < 0:
        print("It's Negative")
    elif num == 0:
        print("It's Zero")
    else:
        print("It's Positive")
    # return type(num)

print(sign(74))
print(sign(0))
print(sign(-23))