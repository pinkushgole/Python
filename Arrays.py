import array as arr

name="pinkush  gole"
print(type(name))


ar=arr.array("i",[1,2,3,4])
print(ar) 

for value in ar:
    print(value)

print(ar.typecode)

print(type(ar))


ar=arr.array("i",[1,2,3,4,12,4,5,7876])
print(f"length of array : {len(ar)}")
print(ar[2])

for i in range(0,len(ar)):
    print(ar[i])

#  adding any elements in arry (user insert to add element in index)(append add elements in last index )

a=arr.array("i",[1,2,3,4,5,6])

for i in range(0,len(a)):
    print(a[i],end=" ")
    
print("\n")

a.insert(1,1)
a.insert(0,10)
a.append(18)
for i in range(0,len(a)):
    print(a[i],end=" ")

#  removing elements 
a=arr.array("i",[1,2,3,4,5,6,9,23,9])
for i in range(0,len(a)):
     print(a[i],end=" ")
print("\n")

a.remove(9)
a.pop()

for i in range(0,len(a)):
     print(a[i],end=" ")

# sliceing elements

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)


# Searching Element in an Array

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
print("\r")
print("The index of 1st occurrence of 2 is : ", end="")
print(a.index(21))

# Updating Elements in a Array

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a= arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
print("\r")
a[4]=13
for i in (a):
    print(i, end=" ")


#   Counting Elements in a Array

l = [1, 2, 3, 4, 5, 6, 7,23,3,3,3, 8, 9, 10]
a= arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
print("\r")
count=a.count(3)
print(f"accourance of number  in giver array : {count}")

#    Reversing Elements in a Array

l = [1, 2, 3, 4, 5, 6, 7,23,3,3,3, 8, 9, 10]
a= arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
print("\r")

a.reverse()

for i in (a):
    print(i, end=" ")
print("\r")



#    Extend Element from Array

l = [1, 2, 3, 4, 5, 6, 7,23,3,3,3, 8, 9, 10]
a= arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
print("\r")

a.extend([2,5,6,98,56,34,12,34])

for i in (a):
    print(i, end=" ")
print("\r")


