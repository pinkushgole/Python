# question 1 age grop chaeck

age=int(input("Enter a age :"))
if age<=13:
    print("Child")
elif age>=14 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adults")
else :
    print("Senior")


# question 2  movie ticketnpricing
age=int(input("Enter a age :"))
day="wednesday"
price=12 if age >=18 else 8

if day=="wednesday":
    price=price-2
print(price)

#   question 3 grade calculator 
score=int(input("Enter score :"))
if score>=101:
    print("Please Valid score submit!!!")
    exit()

if score >=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else :
    grade="E"
print(f"Garde :{grade}")

#  question 4 fruits Ripeness Checker
fruit="Banana"
color=input("Enter Color :")

if fruit=="Banana":
    if color=="Green":
        print("Unripe")
    elif color=="Yellow":
        print("Ripe")
    elif color=="Brown":
        print("OverRipe")
else:
    print("Anoter fruits not available")

# Question 5 Weather Activity suggestion
weather="Sunnay"
if weather=="Sunnay":
    print("Go for a walk")
elif weather=="Rainy":
    print("Read a Book")
elif weather=="Sonwy":
    print("Build a snownman") 

# Questions 6 Transporatation Mode Selection

distance=int(input("Enter a distance : "))
if distance<3:
    print("Walk")
elif distance<15:
    print("Bike")
elif distance>15:
    print("Car")


# Questions 7  coffe customization
order_size="Medium"
extra_sort=True

if extra_sort:
    coffee=order_size+" coffee with an extra shot"
else:
    coffee=order_size+"coffee"

print("Order:",coffee)

# Questions 8  password checker

password=input("Enter your password :")
len_Password=len(password)
if len_Password<6:
    print("Your Password is Weak")
elif len_Password<10:
    print("Password Medium Strong")
else :
    print("password are Strong")

#  question 9 Pet Food Recommendation
dog_age=int(input("Enter dog age : "))

if dog_age<2:
    print("Puppy Food!!!")
else :
    print("Adults Food!!!")
 
