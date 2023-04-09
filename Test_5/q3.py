# Write a function to find the sum of the cube of elements in a list. The list is received as 
# an argument to the function and it should return the sum.

def func(list):
    return sum(i ** 3 for i in list)
list = [8,2,3,4,5]
print(func(list))