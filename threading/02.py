import threading
import time

start=time.perf_counter()

def do_somthing():
    print("sleeping 1 sec")
    time.sleep(1)
    print("done sleeping")

t1=threading.Thread(target=do_somthing)
t2=threading.Thread(target=do_somthing)
t1.start()
t2.start()
t1.join()
t2.join()
finish= time.perf_counter()

print(f'Finished in {round(finish-start,2)} secs')