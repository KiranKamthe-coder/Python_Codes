# Write a program which accept one number and returns True if  number is Odd otherwise false

OddTrue = lambda value: value%2==1


def main():
    print("Enter number")
    no = int(input())

    Ans = OddTrue(no)

    print(Ans)

if(__name__ == "__main__"):
    main()