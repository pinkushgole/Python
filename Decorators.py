def greet1(fx):
    def mx():
        print("GoOd Morning")
        fx()
        print("finish the funaction")
    return mx

@greet1
def hello():
    print("hello world")


greet1(hello())
hello()

#  with arguments

def greet(fx):
    def mx(*ar,**b):
        print("GoOd Morning")
        fx(*ar,**b)
        print("finish the funaction")
    return mx

@greet
def hi(a,b):
    print(a+b)



hi(12,45)

