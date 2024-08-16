# def greet1(fx):
#     def mx():
#         print("GoOd Morning")
#         fx()
#         print("finish the funaction")
#     return mx 

# @greet1
# def hello():
#     print("hello world")


# greet1(hello())
# hello()

# #  with arguments

# def greet(fx):
#     def mx(*ar,**b):
#         print("GoOd Morning")
#         fx(*ar,**b)
#         print("finish the funaction")
#     return mx

# @greet
# def hi(a,b):
#     print(a+b)



# hi(12,45)

#  qoestion 1  Timing function execution

# import time
 
# def timer(func):
#     def wrapper(*args,**kwrags):
#         start=time.time()
#         result =func(*args,**kwrags)
#         end=time.time()
#         print(f"time of {func.__name__} {end-start} time")
#         return result
#     return wrapper
# @timer
# def exampal(n):
#     time.sleep(n)

# exampal(2)

# debuging function calls

# def debug(func):
#    def wrapper(*args,**kwargs):
#       arg_value=', '.join(arg for arg in args)
#       print(f"calling : {func.__name__} with args value : {arg_value}")
#       print(type(arg_value))
#       func(*args,**kwargs)
   
#    return wrapper
   
# @debug
# def greet(name,greeting="Hello"):
#    print(f"{greeting} , {name}") 

# greet("pinkush","chai")

#  chache  value return
import time

def cache(fun):
    cache_value={}
    print(f"cach value : {cache_value}")
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        rs=fun(*args)
        cache_value[args]=rs
        return rs
    return wrapper

@cache
def long_running(a,b):
    time.sleep(4)
    return a+b


print(long_running(2,3))
print(long_running(4,3))
