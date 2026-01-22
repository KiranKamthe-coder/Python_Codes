# Write a progrme to accept one number and check whether it is perfect number or not : input 6 output perfect number

def main():
    print("Enter the number : ")
    no = int(input())

    CheckPerfect_Temp= no
    result =0

    for i in range(1,no):
        if(no % i ==0):
            result=result+i


    if(CheckPerfect_Temp ==  result):
        print("Number is perfect number : ", CheckPerfect_Temp)
    else:
        print("Number is not perfect number : ",CheckPerfect_Temp)    


if(__name__ == "__main__"):
    main()