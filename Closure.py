x=10
def fun(num):
    print(f"num value : {num}")
    def fun1(x):
        print(f"value of x : {x}")
        return x**num
    return fun1

f=fun(2)
print(f(3))