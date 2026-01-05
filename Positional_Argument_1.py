def display(A, B, C, D):
    print(A,B,C,D)

def main():
    #display(10,20) # not allowed arguments and parameters count mismatch --less arguments 
    #display(10,20,30,40,50) # not allowed arguments and parameters count mismatch -- extra arguments
    display(10,20,30,40) # Allowed

if(__name__=="__main__"):
    main()