import os

# create new folder in current directory
if(not os.path.exists("osdirectory")):
    os.mkdir("osdirectory")

# make 100 folder inside osdirectory folder
for i in range(0,100):
    os.rename(f"osdirectory/code {i+1}",f"osdirectory/pinkush {i+1}")  

# check haw may folder in osdirectory folder
folder=os.listdir("osdirectory")
print(folder)

# return current working dir
print(os.getcwd())
# change dir
os.chdir("/users")
print(os.getcwd())


