# Write a progrme to accept one number and prins that many numbers in reverse order  input 5 output 5 4 3 2 1

def main():
    print("Enter one number : ")

    no = int(input())

    for i in range(no,0,-1):
        print(i)
    
if(__name__ == "__main__"):
    main()