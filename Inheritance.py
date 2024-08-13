class Student:
    def __init__(self,name="namen",roll=0):
        self._name=name
        self._roll=roll
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self ,name):     
        self._name=name
    
    @property
    def roll(self):
        return self._roll
        

    @roll.setter
    def roll(self,roll):
        self._roll=roll

    def __str__(self):
        return f"name:{self._name}, roll.no:{self._roll}"


class Programmer(Student):
    def show(self):
        print("this in programmer class and inherit student class")

stu=Student()
stu.name="Pinkush"
stu.roll=1002
print(stu)

p=Programmer("Raja",111)
print(p.name,p.roll)
p.show()