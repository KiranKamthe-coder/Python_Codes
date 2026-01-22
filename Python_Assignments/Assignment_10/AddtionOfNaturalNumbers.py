# Write a program which accept one number and print sum of first N natural numbers

def main():
    print("Enter the number : ")
    no = int(input())    
    
    result = 0
    for i in range(no+1):
        result = result + i

    print("Addtion of first N natrual numbers is : ", result) 
   
if(__name__ == "__main__"):
    main()