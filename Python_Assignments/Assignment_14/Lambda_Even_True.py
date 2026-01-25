# Write a program which accept one number and returns True if  number is even otherwise false

EvenTrue = lambda value: value%2==0 


def main():
    print("Enter number")
    no = int(input())

    Ans = EvenTrue(no)

    print(Ans)

if(__name__ == "__main__"):
    main()