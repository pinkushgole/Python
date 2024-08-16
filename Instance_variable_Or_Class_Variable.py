class Student:
    Collage_Name="Davv,indore"   
    def __init__(self,name="Abc",roll=12):
        self._name=name
        self._roll=roll
    
    def __str__(self):
        return f"name : {self._name} ,Collage Name :{Student.Collage_Name} , roll No : {self._roll}"
 
st=Student("hitesh",1)

print(st) 