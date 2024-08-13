class Student:
    def show(self):
        print("this is Student class")

class College:
     def show(self):
        print("this is college class")

s=Student()
s.show()

c=College()
c.show()
s=College()
s.show()