
l=[2,1,3,4,5,"hi","hello"]
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[5][0])

#nagetive indexing
l=[2,1,3,4,5,"hi","hello"]
print(l[-1])

# Check if Item Exists
l=[2,1,3,4,5,"hi","hello"]
if 22 in l:
    print("elements is present")
else:
    print("nhi hai")

l=[2,1,3,4,5,"hi","hello"]
print(l[0:len(l)])

#List Comprehension

l=[1,2,3,4,5,6,7,8,9]
l=[i*2 for i in range(10) if i%2==0]
print(l)
l.append(12)
print(l)

l=[13,22,3,4,5,6,7,8,9,1,2]
l.sort(reverse=True)
l.reverse()
print(l.index(3))
l.insert(2,123)
print(l)