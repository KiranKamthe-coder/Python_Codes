# Write a program which accept one number and print factorial of that number

def main():
    print("Enter the number : ")
    no = int(input())    
    
    result = 1
    for i in range(1, no+1):
        #print("Inside for")
        result = result * i

    print("Factorial of number is : ", result) 
   
if(__name__ == "__main__"):
    main()