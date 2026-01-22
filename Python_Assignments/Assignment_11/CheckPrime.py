# Write a program which accepts one number and check whether it is prime or not.

def main():
    print("Enter the number : ")
    no = int(input())
    flg = 0

    for i in range(2,no):
        if(no % i == 0 ):
            flg = 1
            break
        
    if(flg == 1):
        print("No is not prime")
    else:
        print("No is prime")

if(__name__ == "__main__"):
    main()