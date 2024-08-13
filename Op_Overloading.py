class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return Vector(self.i+x.i, self.j+x.j ,self.k+x.k)

v=Vector(1,6,4)
print(v)
v1=Vector(13,26,24)
print(v1)
print(v+v1)
print(type(v+v1))