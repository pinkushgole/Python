x=10
def fun(num):
    print(num)
    def fun1(x):
        print(x)
        return x**num
    return fun1

f=fun(2)
print(f(3))