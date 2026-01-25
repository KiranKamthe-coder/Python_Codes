# write a lambda function using reduce() which accepts list of numbers and returns addition of numbers

from functools import reduce

ListAddition = lambda Data : reduce(lambda x,y:x+y,Data)

def main():
    Data=list()

    No=int(input("How many numbers you want in list : "))
    print("Enter the list numbers : ")

    for i in range(No):
        ListNo = int(input(f"Enter the number {i+1} : "))
        Data.append(ListNo)

    print("Addition of list Numbers : ",ListAddition(Data))

if(__name__ == "__main__"):
    main()