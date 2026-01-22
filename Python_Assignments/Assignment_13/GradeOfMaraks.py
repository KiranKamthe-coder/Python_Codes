# Write a progrme to accept marks and diplay grades conditions >=75 : Distintion >=60 First class >=50 : Second class <50 : Fail

def main():
    print("Enter the Marks : ")
    Marks = int(input())

    if(Marks >=75):
        print("Distinction")
    elif(Marks>=60 and Marks<75):
        print("First Class")
    elif(Marks>=50 and Marks<60):
        print("Second Class")
    elif(Marks < 50):
        print("Fail")
    
if(__name__ == "__main__"):
    main()