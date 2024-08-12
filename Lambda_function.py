
double=lambda x:x*2
print(double(4))

multi=lambda a,b:a*b
print(multi(12,3))

multi=lambda a,b,c:a*b*c
print(multi(12,3,1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def app(fx,value):
  return 10*fx(value)

print(app(double,12))
