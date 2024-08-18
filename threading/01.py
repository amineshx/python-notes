import time

start=time.perf_counter()

def do_somthing():
    print("sleeping 1 sec")
    time.sleep(1)
    print("done sleeping")

do_somthing()
do_somthing()

finish= time.perf_counter()

print(f'Finished in {round(finish-start,2)} secs')