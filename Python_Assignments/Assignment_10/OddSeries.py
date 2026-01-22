# Write a program which accept one number and print odd numbers till that number

def main():
    print("Enter the number : ")
    no = int(input())    
        
    for i in range(1, no+1):
        if(i % 2 == 1):
            print(i)
           
if(__name__ == "__main__"):
    main()