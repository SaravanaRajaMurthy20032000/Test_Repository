# 3. Write a program "list_grouping.py" that takes a list and splits into smaller lists of given size. For example,
# if lst = [1, 2, 3, 4, 5, 6], size = 2, it should return [[1, 2], [3,4], [5,6]] and
# if lst = [1,2,3,4,5,6,7,8,9], size = 4 then it should return [[1,2,3,4],[5,6,7,8],[9]]

def list_grouping(lst, size):
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i+size])
    return result

lst = [1,2,3,4,5,6]
size = 2
res = list_grouping(lst,size)
print(res)

lst = [1,2,3,4,5,6,7,8,9,10]
size = 4
res = list_grouping(lst,size)
print(res)