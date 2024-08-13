
# class Company:
#     comapny_name="apple"

#     def show(self):
#         print(f"Person name : {self.name} and company name: {self.comapny_name}")
#     @classmethod
#     def change_com_name(cls,cname):
#         cls.comapny_name=cname

# c=Company()
# c.name="pinkush"
# c.show()
# c.change_com_name("google")
# c.show()
# print(Company.comapny_name)


#  class methods as a alternative constructors (data directly nhi diya jayega ki dusre form me hoga to usko change karke apne according pass karna )

class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
     
    @classmethod
    def formateString(cls,string):
          name, salary = string.split("-")
          return cls(name,int(salary))
    
e=Emp("pinkush",123)
print(e.name)
print(e.salary)
str="raja-1234211"
e2=Emp.formateString(str)
print(e2.name)
print(e2.salary)

