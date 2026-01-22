# Write a program which accepts one number and check whether it is palidrome or not


def main():
    print("Enter the number : ")
    no = int(input())
    Remainder=0
    ReverseNo=0
    no_Temp = no
    

    while(no>0):
        Remainder = no % 10
        no =  no // 10

        ReverseNo =  (ReverseNo*10) + Remainder
        
    if(no_Temp == ReverseNo):
        print("Number is palindorme :", ReverseNo)
    else:
        print("Number is not palindorme :", no_Temp)



if(__name__ == "__main__"):
    main()