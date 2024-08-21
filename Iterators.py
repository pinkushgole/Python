
list=[1,3,5,7,4,2]
myit=iter(list)

print(next(myit))

print(next(myit))

print(next(myit))

print(next(myit))

print(next(myit))

print(next(myit))
print(next(myit))


# Strings are also iterable objects, containing a sequence of character
str="my name is pinkush"
it_str=iter(str)
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class Itr:
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        #  x = self.a
        #  self.a += 1
        #  return x
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
          raise StopIteration
    
myclass = Itr()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

