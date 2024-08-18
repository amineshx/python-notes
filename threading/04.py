import concurrent.futures
import time

start=time.perf_counter()

def do_somthing(seconds):
    print(f"sleeping {seconds} sec")
    time.sleep(seconds)
    return f"done sleeping {seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,3,2,4,1]
    result=[ executor.submit(do_somthing,sec) for sec in secs]
    # for res in result:
    #     print(res.result())
    for f in concurrent.futures.as_completed(result):
        print(f.result())

# threads=[]
# for _ in range(10):
#     t=threading.Thread(target=do_somthing, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish= time.perf_counter()

print(f'Finished in {round(finish-start,2)} secs')