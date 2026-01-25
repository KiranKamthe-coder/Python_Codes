# write a lambda function using filter() which accepts list of numbers and returns count of even numbers

from functools import reduce

CountEven = lambda Data : len(list(filter(lambda x:(x%2==0),Data)))

def main():
    Data=list()

    No=int(input("How many numbers you want in list : "))
    print("Enter the list numbers : ")

    for i in range(No):
        ListNo = int(input(f"Enter the number {i+1} : "))
        Data.append(ListNo)

    print("Count of even numbers from list is : ",CountEven(Data))

if(__name__ == "__main__"):
    main()