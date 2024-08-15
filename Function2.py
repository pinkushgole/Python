#  basic function sentex
def square_number(n):
    return n**2
print(square_number(4))

# function with multipale parameters

def add(a,b):
    return a+b
print(add(14,2))

# polymorphism in function
def multiplication(a,b):
    return a*b

print(multiplication(12,2))
print(multiplication("a1gg",2))
print(multiplication(2,"b"))

#  return multiple value
import math
def ciral(radius):
    area=math.pi*radius**2
    cf=2*math.pi*radius
    return area,cf

area,cf=ciral(3)
print(f"area : {area} cf : {cf}")


#  defult paremater

def greet(name="garm"):
    return f"hello ,{name}"

print(greet())

# lambda function
number=lambda x:x**3
print(number(2))

#  user of *args
def sum_args(*args):
    return sum(args)

print(sum_args(1,2,3,4))

# user **kwargs
def add(**num):
    print(num)

add(name="1",name1="2")

#  generate function yield

def even(limit):
    for i in range(2,limit+1,2):
        yield i

even(18)


