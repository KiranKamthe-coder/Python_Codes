# write a lambda function using reduce() which accepts list of numbers and returns maximum number

from functools import reduce

ListMax = lambda Data: reduce(lambda x, y: x if x > y else y, Data)

def main():
    Data=list()

    No=int(input("How many numbers you want in list : "))
    print("Enter the list numbers : ")

    for i in range(No):
        ListNo = int(input(f"Enter the number {i+1} : "))
        Data.append(ListNo)

    print("Maximum Number is  : ",ListMax(Data))

if(__name__ == "__main__"):
    main()