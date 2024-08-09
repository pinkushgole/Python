# def add(a,b):
#     add=a+b
#     print(add)

# def mul(a,b):
#    print("multication function")
#    pass

# a=10
# b=199
# add(a,b)
# mul(a,b)

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


#Avrage
# def avg(a,b):
#     print("avrage of two numbers : ",(a+b)/2);

# avg(12,3)

#   Default Parameter Value
# def division(a=12,b=13):
#     print(a/b)

# division(12,12)
# division(10,2)
# division()


#    Keyword Arguments order of arrugument can be change
# def add(a,b,c):
#     print("Submision of all elements : ",a+b+c)

# add(b=23,c=1,a=10)

#   required argument  (value dena hi padega jeseki a is required arguments)
# def add1(a,b=1):
#     print(a+b)

# add1(12)

#  variable length arguments
# # 1 convert as tuple
# def add(*num):
#     print(num)

# add(1,2,3)

# 2 convert as dict
# def add(**num):
#     print(num)

# add(1,2,3)


#    Return Values
def avg(a,b):
    c=(a+b)/2
    return c

c=avg(12,45)
print(c)


