def main():
    Size = 0
    print("Enter the number of elements: ")
    Size = int(input())
    Data = list()

    print("Enter the elements")
    value = 0
    for i in range(Size):
        value = int(input())
        Data.append(value)

    sum = 0

    for i in range(Size):
        sum = sum + Data[i]
        print ("Summation is : ", sum)

if (__name__=="__main__"):
    main()
    