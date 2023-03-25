### 
# Test paper on List, Tuple and Dictionary in Python
###

"""
********* Count negative numbers *********

Write a program to return the number of negative numbers in the given list.
Sample Input: 
    [5, -1, -2, 0, 3]
Expected Output: 
    2

"""
l = [5,-1,-2,0,3]
l1 = 0
for i in l:
    if i < 0:
        l1 += 1
print(l1)



"""
********* Gnereate Boolean List *********

Write a program to return a list with the same length as the given list L, 
where the value at index i is True if L[i] is greater than given number, and 
False otherwise.

Sample Input: 
    L = [1, 2, 3, 4], num = 2
Expected Output: 
    [False, False, True, True]
    
"""

L = [1, 2, 3, 4]
num = 2
res = []
for i in L:
    if i > num:
        res.append(True)
    else:
        res.append(False)    
print(res)



"""
********* Remove all elements having duplicates *********

Write a program to print a list of all elements in a list that have 
only a single occurrence. 

For example, if the contents of the list is 
    [7, 5, 5, 1, 6, 7, 8, 7, 6], 
it should return 
    [1, 8]

"""

l = [7, 5, 5, 1, 6, 7, 8, 7, 6]
c = []
for i in l:
    if l.count(i) == 1:
        c.append(i)
print(c)



"""
********* Helping with the Budget *********

John has a hard time keeping his budget. Write a program to help him analyze his spendings. 
You are given a list with John's spendings for each month. 
Go through the list, and count the number of times...
    a. the spendings were low (< 1000.0)
    b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
    c. the spendings were high (> 2500.0)
Then, print the following to the output:
    Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.

Let spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 
                    2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

"""

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_spendings = []
normal_spendings = []
high_spendings = []

for i in spendings:
    if i < 1000.0:
        low_spendings.append(i)
    elif 1000.0 < i < 2500.0:
        normal_spendings.append(i)
    elif i > 2500.0:
        high_spendings.append(i)
print(f"No.of.Months with Low spendings are {low_spendings}")
print(f"No.of.Months with Normal spendings are {normal_spendings}")
print(f"No.of.Months with High spendings are {high_spendings}")


"""
********* All Roads Lead to Rome ********* 

You are given a list with various flight connections in Europe. Each connection is represented as a tuple with the following elements:
    (city_from, city_to, time)
For example, the following tuple represents a flight from Amsterdam to Dublin which takes 100 minutes:
    ('Amsterdam', 'Dublin', 100)

Your task is to go through all the routes in a loop and check how many of them lead to Rome (i.e. how many of them have city_to equal to 'Rome'). 
Among the routes to Rome, you should also calculate the average flight time. Print the following to the output:
    `{} connections lead to Rome with an average flight time of {} minutes`
Here you need to replace {} with "the number of connections" and "the average flight time".

Let connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
"""
l = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

count = 0
t_time = 0

for i in l:
    if i[1] == "Rome":
        count += 1
#         t_time += l[2]

# avg_time = t_time / count


"""
A company allows its employees to work in a hybrid model. Here given a dictionary of employee's work status on a day as input,
    statuses = {"Alice": "online", 
                "Bob": "offline", 
                "Eve": "online", 
                "Ravi": "online", 
                "sneha": "offline", 
                "vinod": "online", 
                "dheepika": "online"}
Write a program that should return the number of people who are online and Print the following to the output:
    `{} employees are working online`
Here you need to replace {} with "the number of employees who are online"

"""

statuses = {
            "Alice": "online", 
            "Bob": "offline", 
            "Eve": "online", 
            "Ravi": "online", 
            "sneha": "offline", 
            "vinod": "online", 
            "dheepika": "online"
}
online = 0
# offline = 0
for i in statuses.values():
    if i == "online":
        online += 1
print(f"{online} employees are working online")


"""
Write a program that reads a string from the user and create a dictionary having a key as word length 
and the value is the count of words of that length. 
For example, if the user enters 
    'A fat cat is on the mat'
    
        Word    Word length
        A       1
        fat     3
        cat     3
        is      2
        on      2
        the     3
        mat     3

The print the following to the output: 
    {1:1, 3:4, 2:2}
In the output, keys are word lengths and values are their count.

"""
str = input("enter the string: ")
words = str.split()
d = {}
for i in words:
    x = len(i)
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
print(d)