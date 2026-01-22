
def main():
    ans=0

    try:
        print("Inside try : ")
        print("Enter first number : ")
        no1=int(input())
        print("Enter second number : ")
        no2=int(input())
        
        ans =no1/no2
        
    except ZeroDivisionError as zobj:
        print("Inside except : ",zobj)

    except ValueError as vobj:
        print("Inside except : ",vobj)

    except Exception as eobj:
        print("Inside except : ",eobj)    

    finally:
        print("Inside finally : ")

    print("Division is : ",ans)

if(__name__=="__main__"):
    main()