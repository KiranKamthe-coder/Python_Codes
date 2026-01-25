# Write a lambda function which accepts three numbers and return largest number 

Largest=lambda value1,value2,value3: max(value1,value2,value3)

def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())    
    print("Enter third number")
    no3 = int(input())

    Ans = Largest(no1,no2,no3)

    print("Largest number is : ",Ans)

if(__name__ == "__main__"):
    main() 