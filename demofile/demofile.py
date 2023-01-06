import os
from time import sleep,perf_counter
from threading import Thread
def task(f,f1,f2):
    f=open("text_file1.txt","r")
    sleep(1)
    f1=open("text_file2.txt", "r")
    sleep(1)
    f2=open("text_file3.txt", "r")
    sleep(1)
    print("task done")
start_time=perf_counter()
t1=Thread(target=task,f)
t2=Thread(target=task,f1)
t3=Thread(target=task,f2)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end_time=perf_counter()
print(f'{end_time-start_time} seconds to executed')