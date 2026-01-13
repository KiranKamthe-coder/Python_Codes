from sys import getsizeof


def main():

    No1 = 0 
    print("Enter the Number : ")
    No1= int(input())

    print("Data type of variable is : ",type(No1))
    print("Memory address of variable is : ",id(No1))
    print("Size of variable is : ",getsizeof(No1))


if(__name__=="__main__"):
    main()