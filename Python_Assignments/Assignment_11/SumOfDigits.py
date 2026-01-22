# Write a program which accepts one number and print sum of digits in that number no =123 op=6

def main():
    print("Enter the number : ")
    no = int(input())
    Remainder=0
    DigitSum=0

    while(no>0):
        Remainder = no % 10
        no =  no // 10

        DigitSum = DigitSum + Remainder
        
        

    print("Digit sum is :", DigitSum)


if(__name__ == "__main__"):
    main()