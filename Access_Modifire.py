#  public access modifire

class Access:
    def __init__(self):
        self.name="pinkush"

a=Access()
print(a.name)

# Protected Access Modifier:

class Stu:
    def __init__(self):
        self.__name="protrctrd access modifire"

s = Stu()
#print(a.__name)  #not access directly
print(s._Stu__name) 


# Private Access Modifier:

class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):

        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self):

        # accessing private member function
        self.__displayDetails()


# creating object
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()