import threading
import time

def sumeven(no):
    sum=0
    for i in range(2,no+1,2):
        sum=sum+i

    print("Even sum is : ",sum)

    
def sumodd(no):
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i

    print("odd sum is : ",sum)

def main():
    start_time =time.time()
    sumeven(10000000000)
    sumodd(100000000000)
    end_time=time.time()

    print("time required :", end_time-start_time)


if(__name__ == "__main__"):
    main()