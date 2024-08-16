# x=[12,3,4,5,1]
# print(dir(x))
# print(x.__add__)
# print(x.pop())

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person("Raja",12)
print(p.__dict__)

# print(help(Person))