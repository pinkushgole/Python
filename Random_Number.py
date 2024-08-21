from numpy import random

# gernratr int random number
x=random.randint(199)
print(x)

# Generate Random Float
x=random.rand()
print(x)

# generate random array

x1=random.randint(100,size=10)
print(x1)
print(type(x1))

# Generate a 2-D array 

twod=random.randint(10,size=(3,3))
print(twod)

# Return one of the values in an array:

ch=random.choice([3,2])
print(ch)