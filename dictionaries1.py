
dic={"name":"pinkush" ,"age":23,"cource":"BCA"}
print(dic)
print(dic["age"])
print(dic.get("agea"))

for keys in dic:
    print(keys,dic[keys])

print(dic.items())

for key,value in dic.items():
    print(f"keys:{key}, values:{value}")

if "name" in dic:
    print("yes mil gai") 
print(len(dic))