# write a lambda function using filter() which accepts list of numbers and returns list of even numbers

CheckEven = lambda Data : list(filter(lambda x: x%2==0, Data))

def main():
    Data=list()

    No=int(input("How many numbers you want in list : "))
    print("Enter the list numbers : ")

    for i in range(No):
        ListNo = int(input(f"Enter the number {i+1} : "))
        Data.append(ListNo)

    print("Even Numbers from the list are : ",CheckEven(Data))

if(__name__ == "__main__"):
    main()