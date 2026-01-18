import os

def factorial(no):
    fact=1
    for i in range(1,no+1):
        print (i)
        fact=fact*i
    return fact

def main():
    value = int(input("Enter the number "))
    ret=factorial(value)

    print("factorial is : ",ret)

if(__name__ == "__main__"):
    main()