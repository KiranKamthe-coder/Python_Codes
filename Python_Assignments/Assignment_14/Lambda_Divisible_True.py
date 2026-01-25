# Write a program which accept one number and returns True if  number is divisible by 5 otherwise false

Divisible = lambda value: value%5==0


def main():
    print("Enter number")
    no = int(input())

    Ans = Divisible(no)

    print(Ans)

if(__name__ == "__main__"):
    main()