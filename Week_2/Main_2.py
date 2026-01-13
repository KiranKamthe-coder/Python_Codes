def Multiplication(Value1, Value2):
    Ans = 0 #Local variable
    Ans = Value1 * Value2
    return Ans

#No1 = 0, No2=0, Result =0 # not allowed
def main():
    No1 = 0
    No2=0
    Result =0 

    print("Enter first number : ")
    No1=int(input())

    print("Enter second Number : ")
    No2= int(input())

    Result= Multiplication(No1, No2)
    print("Multiplication is : ", Result)

if __name__=="__main__":
    main()  

