# Write a program which accept two numbers and returns maximum number

Maxno = lambda value1,value2: value1 if value1>value2 else value2


def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())

    Ans = Maxno(no1,no2)

    print("Maximum number is : ",Ans)

if(__name__ == "__main__"):
    main()