class Person:
    name="Abc"
    networth=10000
    def info(self):
        print(f"name : {self.name} , networth : {self.networth}")


a=Person()
# a.name="CBA"
a.info()
b=Person()
b.name="pinkush"
b.networth=12333
b.info()


#  constructors

class Student:
     def __init__(self,name,roll):
         self.name=name
         self.roll=roll
         print("add pass succesfully!!!!!!")
     
     def show(self):
         print(f"name:{self.name} , roll no:{self.roll}")


a=Student("Raja",123)
a.show()
b=Student("Aj",123)
b.show()

#    Getters and setters

class Geek: 
    def __init__(self, age = 0): 
         self._age = age 
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 


g=Geek()
g.set_age(12)
print(g.get_age())


class Geeks: 
     def __init__(self): 
          self._age = 0
    
     @property
     def age(self): 
         print("getter method called") 
         return self._age 
    
     @age.setter 
     def age(self, a): 
         if(a < 18): 
            raise ValueError("Sorry you age is below eligibility criteria") 
         print("setter method called") 
         self._age = a 

mark = Geeks() 
  
mark.age = 19
  
print(mark.age) 