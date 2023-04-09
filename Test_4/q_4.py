# Write a program "dups.py" to print a list with all duplicates in the given list. 
# For example, if lst=[1, 3, 2, 1, 2, 5, 6] it should return [1, 2].

lst = [1, 3, 2, 1, 2, 5, 6]
res = []
for i in lst:
    if lst.count(i) > 1:
        res.append(i)
res = set(res)
print(f"The Duplicate number is {list(res)}")