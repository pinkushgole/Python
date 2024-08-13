class ParentClass:
    def parent(self):
        print("this is parent class!!!")

class ChildClass(ParentClass):
    def parent(self):
        print("this is chaild class parent mathed")
        return super().parent()
    def child(self):
        print("this is chaild class !!!")
        super().parent()

p=ParentClass()
p.parent()
c=ChildClass()
c.child() 
c.parent()