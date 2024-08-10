#   creating a set and use for loop
s={2,5,3,6,8,6,31,7,65432,345678,888,65,43}
# print(s)
# for i in s:
#     print(i*2)

s={1,2,3,4,5}
#print(s)
s.add(12)# aad new elements
s.add(8)
#print(s)

#union
s={1,3,5,6,7}
s1={2,3,5,6,7,7,8,9,1}
s3=s.union(s1)
s.update(s1)
# print(s)

# intersection
s={1,3,5,6,7,12}
s1={2,3,5,6,7,7,8,9,1}
#print(s.intersection(s1))
s1.intersection_update(s)
print(s1)

thisset = {"apple", "banana", "cherry"}

# thisset.remove("bananas")

print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)