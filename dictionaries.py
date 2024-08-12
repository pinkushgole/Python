dic={
    "1":"sunday",
    "2":"monday",
    "3":"tuesday"
}
print(dic)
print(type(dic))
dic={

}
print(dic)
print(type(dic))

dic={
    1:"sunday",
    2:"monday",
    3:"tuesday"
}
print(dic[1])
print(dic.get(13))

dic={
    1:"sunday",
    2:"monday",
    3:"tuesday"
}
print(dic.keys())

dic={12:100,
     2:200,
     3:300}
print(dic.keys())
print(dic.values())

for keys in dic.keys():
    print(f"{keys} value of {dic[keys]}")

for keys , values in dic.items():
    print(f"{keys} value of {values }")

print(dic.items())

dic={12:100,
     2:200,
     3:300}

print(dic)
dic.update({3:233})
dic.pop(12)
dic.popitem()
del dic[12]
print(dic)

