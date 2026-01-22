# Write a progrme to accept one number and prins that many numbers starting form 1: input 12 output 1 2 3 4 5 6 7 8 9 10 11 12

def main():
    print("Enter one number : ")

    no = int(input())

    for i in range(1,no+1):
        print(i)
    
if(__name__ == "__main__"):
    main()