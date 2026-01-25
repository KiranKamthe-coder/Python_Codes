# Write a lambda function using map() which accepts a list of numbers and returns a squares of each number

def Square(Data):
    Result=list()
    for i in range(len(Data)):
        Ans=Data[i]*Data[i]
        Result.append(Ans)
    return Result


def main():

    print("How many numbers you wnat to hold in list :")
    No=int(input())

    print("Enter the list numbers : ")

    Data=list()

    for i in range(No):
        listdate=int(input(f"Enter Number {i+1} : "))
        Data.append(listdate)

    SquareList=Square(Data)
    print("Square of numbers are : ",SquareList)

if(__name__ == "__main__"):
    main()