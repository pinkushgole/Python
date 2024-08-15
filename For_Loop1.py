#  count positive number
list=[1,3,-3,-4,6,-7,54,-9]
count=0
for num in list:
    if num>0:
        count+=1
print(count)

# sun of even numbers
number=10
sum_even=0
for i in range(1,number+1):
    if i%2==0:
        sum_even+=i
print(f"sum of even numbers : {sum_even}")

#  multiplication table given number
number=int(input("Enter a number : "))

for i in range(1,11):
    if(i==5): 
        continue
    else:
        print(f"{number}*{i}={number*i}")

# revere string using loop
name="chai"
revse=""
for ch in name:
    revse=ch+revse
print(revse)

#  find the first non-repeated char
name="teeter"

for char in name:
    if name.count(char)==1:
        print(f"char is : {char}")

#   factorial
num=int(input("Enter a number : "))
fac=1
while num!=0:
    fac*=num
    num-=1
print(f"factorial : {fac}")

#  validate input
while True:
    num=int(input("Enter value  between 1 and 10: "))
    if num>1 and num<10:
        print(" number is right")
        break
    else:
        print("enter a valid number")

#  prime number checker
number=int(input("Enter a prime number : "))
is_prime=True
for i in range(2,int(number/2)):
    if(number%i==0):
        is_prime=False
        break
if is_prime:
    print("Number is prime")
else:
    print("number is not prime")

#  list uniqueness checker
list=["apple","banana","orange","apple1","mango"]

unique_item=set()

for item in list:
    if item in unique_item:
        print("Dublicate :",item)
        break
    unique_item.add(item)

#  Exponential backoff

import time

wait_time=1
max_try=5
attempts=1

while attempts<=max_try:
    print("attempts",attempts,"-wait time ",wait_time)
    if(attempts==max_try):
        exit()
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1