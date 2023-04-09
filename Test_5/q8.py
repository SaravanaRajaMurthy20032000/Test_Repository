# Write a function ‘select_second’ with one argument 'L' which is a list to return the second element of the given list. 
# If the list has no second element, it should return None.

def select_second(L):
    if len(L):
        return L[1]
    else:
        return None
    
print(select_second([1,2,3,4,]))
print(select_second(['a','s','d','f','g']))