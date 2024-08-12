#    Map

def squre(x):
    return x*x

list1=[1,2,3,4,6,7,9,10]
print(list)

newl = list(map(squre,list1))
print(newl)

#   filter
def filter_fun(a):
    return a>4

newl= list(filter(filter_fun,list1))
print(newl)


# reduce
from functools import reduce

newl=reduce(lambda x,y:x+y, list1)
print(newl)

