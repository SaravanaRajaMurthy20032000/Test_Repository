lst = [1, 3, 2, 1, 2, 5, 6]
res = []
for i in lst:
    if lst.count(i) > 1:
        res.append(i)
res = set(res)
print(f"The Duplicate number is {list(res)}")