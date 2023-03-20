# Given this nested list, use indexing to grab the word "hello"
# [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

l = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(l[3])

l1 = l[3]
print(l1)
print(l1[1])

l2 = l1[1]
print(l2)
print(l2[2])

print(f"the final answer is {l2[2]}")
