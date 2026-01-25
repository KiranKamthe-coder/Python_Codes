# Write a program which accept two numbers and returns minimum number

Minno = lambda value1,value2: value1 if value1<value2 else value2


def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())

    Ans = Minno(no1,no2)

    print("Minimum number is : ",Ans)

if(__name__ == "__main__"):
    main()