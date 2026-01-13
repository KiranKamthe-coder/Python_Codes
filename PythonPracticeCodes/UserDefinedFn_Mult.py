def Multiplication(Value1, Value2):
    Result = 0 
    Result = Value1 * Value2
    return Result


def main():
    print("Inside main function : ")

    No1 = 0
    No2= 0
    Answer = 0

    print("Enter fisrt number : ")
    No1= int(input())

    print("Enter second number")
    No2 = int(input())

    Answer = Multiplication (No1, No2)
    print("Multiplication is : ", Answer)


if (__name__ == "__main__"):
    main()