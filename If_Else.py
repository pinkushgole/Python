# age=int(input("Enter your age:"))

# if age>=18:
#     print("you can drive")
# else:
#     print("you con not drive")


#check leap year or not

year=int(input("Enter year :"))

if (year%400==0):
    print(year,"is leap year")
elif (year%100==0):
    print("not a leap year")
elif (year%4==0):
     print(year,"is leap year")
else:
    print("not a leap year")