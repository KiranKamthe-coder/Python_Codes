# write a program which accept one number and check whether it is divisible by 3 and 5 

def main():
    print("Enter the number : ")
    no = int(input())

    if(no % 3 ==0 and no % 5 ==0):
        print("Number is divisible by 3 and 5")
    
if(__name__ == "__main__"):
    main()