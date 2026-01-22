# Write a program which accepts one number and print reverse of that number no =123 op=321

def main():
    print("Enter the number : ")
    no = int(input())
    Remainder=0
    ReverseNo = 0
    

    while(no>0):
        Remainder = no % 10
        no =  no // 10

        ReverseNo =  (ReverseNo*10) + Remainder
        
        

    print("Reverse number is :", ReverseNo)


if(__name__ == "__main__"):
    main()