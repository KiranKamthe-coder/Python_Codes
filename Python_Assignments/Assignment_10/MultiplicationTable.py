# Write a program which accept one number and prints multiplication table of that number

def main():
    print("Enter the number : ")
    no = int(input())
    
    print("Multiplication table is : ")
    for i in range(1, 11):
        print(no * i)

    
if(__name__ == "__main__"):
    main()