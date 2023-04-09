# Write a function "value_sort_by_key.py" to return a list of sorted values based on the keys in the dictionary.
# For example, if {'x':1,'y':2,'a':3} is the dictionary then it should return [3, 1, 2].
d = {'x':1,'y':2,'a':3,'c':8}
s = sorted(d.keys(),key = lambda x:x[0])
print(s)
