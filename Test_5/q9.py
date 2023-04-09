# Write a function half_and_half that takes in a list and change the list such that the elements of the second half are now in the first half. 
# For example, if the list is [10,20,30,40,50,60], then it should return [40,50,60,10,20,30] and if the list is [10,20,30,40,50,60,70], 
# then it should return [50,60,70,40,10,20,30].

def half_and_half(list):
    res = []
    l = list[3:] + list[0:3]
    res.extend(l)
    return res
print(half_and_half([10,20,30,40,50,60]))

def half_center(list):
    res = []
    l = list[4:] + list[3:4] + list[0:3]
    res.extend(l)
    return res
print(half_center([10,20,30,40,50,60,70]))