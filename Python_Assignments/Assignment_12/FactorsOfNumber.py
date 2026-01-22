# Write a progrme to accept one number and print its factors input 12 output 1,2,3,4,6,12

def main():
    print("Enter one number : ")

    no = int(input())

    for i in range(1,no+1):
        if(no % i == 0):
            print("Factor of", no ," is : ", i)
    
if(__name__ == "__main__"):
    main()