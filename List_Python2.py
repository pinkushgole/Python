list=[1,3,"gole",5,2,"pinkush",9]

print(list)
print(list[2:])
print(list)
print(list.pop()) 
list[0]="pink"
list.append(12)
list.append("hello")
print(list)
list[1]=["17",23]
print(list)

for i in list:
    print(i,end=" ")
print("\n")
if "gole" in list:
    print("mere pass hai!!!!!")
print(list.remove(2))
print(list)





