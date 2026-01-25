# Write a lambda function which accepts two numbers and return Multiplication 

Multiplication=lambda value1,value2: value1*value2

def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())

    Ans = Multiplication(no1,no2)

    print("Multiplication is : ",Ans)

if(__name__ == "__main__"):
    main() 