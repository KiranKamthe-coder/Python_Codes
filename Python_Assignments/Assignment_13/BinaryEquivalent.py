# Write a progrme to accept one number print binary equvivalent

def main():
    print("Enter the number : ")
    no = int(input())

    print("Binary equvalent of given number is : ", bin(no)[2:])
if(__name__ == "__main__"):
    main()