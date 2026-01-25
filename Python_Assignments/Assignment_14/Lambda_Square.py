# Write a program which accept one number and returns square of that number

#def Square(value):
#    result=value*value
#    return result

Square = lambda value:value * value


def main():
    print("Enter Number : ")
    no = int(input())

    Ans = Square(no)
    print("Square of the number is : ",Ans)

if(__name__ == "__main__"):
    main()