import json

data={'name':"aj","roll":101}
print(type(data))

json_data=json.dumps(data)
print(json_data)

print(type(json_data))

data1=json.loads(json_data)
print(type(data1))
print(data1)