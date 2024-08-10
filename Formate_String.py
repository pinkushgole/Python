# old way

st="my name is {1}, i am from {0}"
name="pinkush gole"
place="india"
print(st.format(place,name))
print(st)

#  new way
name="pinkush gole"
place="india"
st=f"my name is {name}, i am from {place}"
print(st)