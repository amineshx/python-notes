import concurrent.futures
import time

start=time.perf_counter()

def do_somthing(seconds):
    print(f"sleeping {seconds} sec")
    time.sleep(seconds)
    return f"done sleeping {seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,3,2,4,1]
    result = executor.map(do_somthing,secs)
    for res in result:
        print(res)


finish= time.perf_counter()

print(f'Finished in {round(finish-start,2)} secs')