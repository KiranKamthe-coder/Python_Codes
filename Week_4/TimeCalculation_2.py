import time

def Factorial(no):
    fact = 1
    for i in range(1, no+1):
        print (i)
        fact = fact * i
    return fact

def main():
    value = int(input("Enter the number "))
    start_time=time.time()
    ret=Factorial(value)
    end_time=time.time()
    print("Factorial is : ",ret)
    print("Total execution time is : ",end_time-start_time)

if(__name__ == "__main__"):
    main()