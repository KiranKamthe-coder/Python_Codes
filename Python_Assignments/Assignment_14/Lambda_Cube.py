# Write a program which accept one number and returns cube of that number

Square = lambda value:value * value * value


def main():
    print("Enter Number : ")
    no = int(input())

    Ans = Square(no)
    print("Cube of the number is : ",Ans)

if(__name__ == "__main__"):
    main()