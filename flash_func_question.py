# --Flash Interview questions--
"""1. Write a function that returns the common elements between two given lists."""
def fun(list1,list2):
    num1 = set(list1)
    num2 = set(list2)
    num3 = list(num1 & num2)
    return num3
list1 = [1,2,5,6,7,8]
list2 = [2,1,7,3,4,9]
result = fun(list1,list2)
print(result)

"""2. Given a list of n tuples, where each tuple contains 3 elements. Write a function that return the sorted list of tuples based on second element in each tuple."""
def fun(li):
    num = sorted(li,key=lambda x: x[1])
    return num
res = [(1,2,9),(2,7,3),(8,0,4),(66,88,0)]
print(fun(res))

"""3. Write a function that returns the second highest number in a list."""
def fun(num):
    l1 = sorted(num,reverse=True)
    res = l1[1]
    return res
list = [2,8,3,99,35,4,6]
print(fun(list))

"""4. Write a function that returns the first non-repeating character in a string."""
def char(str):
    for i in str:
        if str.count(i) == 1:
            return i
    return None
l1 = 'harishmani'
print(char(l1))

"""5. Write a function that checks if two strings (for example, listen and silent) are anagrams of each other."""
def fun(str1,str2):
    if (sorted(str1) == sorted(str2)):
        return "Anagram"
    return "Not a Anagram"
str1 = "state"
str2 = "taste"
print(fun(str1,str2))