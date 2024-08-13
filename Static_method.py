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
    def max_value(x, y):
        return max(x, y)
    
obj = MyClass(10)

print(MyClass.max_value(20, 30))  

print(obj.max_value(20, 30)) 