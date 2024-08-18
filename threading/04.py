import concurrent.futures
import time

start=time.perf_counter()

def do_somthing(seconds):
    print(f"sleeping {seconds} sec")
    time.sleep(seconds)
    return "done sleeping"

with concurrent.futures.ThreadPoolExecutor() as executor:
    result=[ executor.submit(do_somthing,1) for _ in range(10)]
    for res in result:
        print(res.result())

# threads=[]
# for _ in range(10):
#     t=threading.Thread(target=do_somthing, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish= time.perf_counter()

print(f'Finished in {round(finish-start,2)} secs')