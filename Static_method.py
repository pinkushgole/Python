class Math:
    def __init__(self,num):
        self.num=num
    
    def show_Number(self):
        print(f"Number : {self.num}")
    
    def add(self,a):
        print(self.num+a)

m=Math(38)
m.show_Number()
m1=Math(12)
m1.add(12)

class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def max_value():
        print("this is static method")
    
obj = MyClass(10)

MyClass.max_value()  

obj.max_value()