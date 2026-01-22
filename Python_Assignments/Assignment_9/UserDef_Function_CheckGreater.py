# Write a program which contains one function ChkGreater() that accepts  two numbers and print the greater number

def ChkGreater(value1, value2):
    if(value1 > value2):
        print(value1, "is greater" )
    else:
        print(value2, "is greater" )

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    ChkGreater(no1, no2)
    
if(__name__ == "__main__"):
    main()