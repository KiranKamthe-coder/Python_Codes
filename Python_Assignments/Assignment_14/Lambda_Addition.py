# Write a lambda function which accepts two numbers and return addition 

Addiotion=lambda value1,value2: value1+value2

def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())

    Ans = Addiotion(no1,no2)

    print("Addition is : ",Ans)

if(__name__ == "__main__"):
    main() 