import threading
import time
from concurrent.futures import ThreadPoolExecutor 

def fun(seconds):
    print(f"time taken to function {seconds}")
    time.sleep(seconds)

# normal code
time1=time.perf_counter()
fun(12)
fun(2)
fun(10)
time2=time.perf_counter()
print(time2-time1)

#  with thread code

t1=threading.Thread(target=fun,args=[5])
t2=threading.Thread(target=fun,args=[7])
t3=threading.Thread(target=fun,args=[2])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print(time2-time1)


# threadpool use

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # first way
        future=executor.submit(fun,5)
        print(future.result())
        future=executor.submit(fun,3)
        print(future.result())
        future=executor.submit(fun,5)
        print(future.result())

        # seconf way
        l=[1,3,2,4]
        results=executor.map(fun,l)
        for rs in results:
            print(rs)

poolingDemo()
