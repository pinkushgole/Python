from time import gmtime, strftime
import time
s = strftime("%a, %d %b %Y %H:%M:%S")
print(s)
# inti=time.time()


# # cureent time
cTime=time.ctime(time.time())
print(cTime)


# sleep method (program ruk jata kuch time ke liye sleep meyhod ke karn)
print("hyy ")
time.sleep(10)
print(9617429049)

# local time
local_time=time.localtime(time.time())
print(f"local time : {local_time}")
print(type(local_time))
s=strftime("%a")
print(s)
