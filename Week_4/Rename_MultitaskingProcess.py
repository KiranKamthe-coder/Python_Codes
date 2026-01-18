import multiprocessing
import time
import os

def sumeven(no):
    sum=0
    print("PID of sumeven : ",os.getpid()) #51
    print("PpID of sumeven : ",os.getppid()) #21
    for i in range(2,no+1,2):
        sum=sum+i

    print("Even sum is : ",sum)

    
def sumodd(no):
    sum=0
    print("PID of sumodd : ",os.getpid()) #101
    print("PpID of sumodd : ",os.getppid()) #21
    for i in range(1,no+1,2):
        sum=sum+i

    print("odd sum is : ",sum)

def main():
    print("PID of main : ",os.getpid()) #21
    print("PpID of main : ",os.getppid()) # CMD 11
    start_time =time.time()
    t1=multiprocessing.Process(target=sumeven,args=(10000,))
    t2=multiprocessing.Process(target=sumodd,args=(10000,))
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    end_time=time.time()

    print("time required :", end_time-start_time)


if(__name__ == "__main__"):
    main()