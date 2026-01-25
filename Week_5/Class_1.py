class demo:
    def __init__(self):
        print("inside constructor")

    def __del__(self):
        print("Inside Destructor")

    
obj = demo() 

print("End of application")
