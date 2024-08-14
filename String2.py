chai="Garm chai"

print(chai)
print(f"single elements : {chai[0]}")


# slicing in string 

chai="0123456789"
print(f"length of give string : {len(chai)}")
print(chai[:])
print(chai[-4])
print(chai[1:])
print(chai[:3])
print(chai[-1:])


# strip in string

chai="   lemon tea   "
print(chai)
print(chai.strip())

#  replace method
chai="rose tea"
print(chai)
new_chai=chai.replace("e","pinkush")
print(new_chai)


# list me convert with split method
chai="tea1, tea2, tea3, tea4"
print(chai)
print(type(chai))
chai_list=chai.split(", ")
print(chai_list)
print(type(chai_list))

# finding a chacher ya word
chai="masala chai"
print(chai.find("chai"))

# count a chachter accorance
chai="masala chai"
print(chai.count("a"))

#  list to string
list=["lemon", "masala", "ginger"]
chai="-".join(list)
print(chai)

# length
chai="masala chai"
print(len(chai))

