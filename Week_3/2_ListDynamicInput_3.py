def Summation(Arr):
    sum = 0
    for i in range(len(Arr)):
        sum = sum + Arr[i]
    return sum

def main():
    Size = 0
    value = 0
    ret = 0

    print("Enter the number of elements: ")
    Size = int(input())
    Data = list()

    print("Enter the elements")
    
    for i in range(Size):
        value = int(input())
        Data.append(value)

    ret = Summation(Data)
    print ("Summation is : ", ret)

if (__name__=="__main__"):
    main()
    