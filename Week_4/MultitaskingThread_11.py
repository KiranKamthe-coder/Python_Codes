import threading

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
    sumeven(10000000)
    sumodd(10000000)


if(__name__ == "__main__"):
    main()