import gc

class demo:
    def __init__(self):
        print("inside constructor")

    def __del__(self):
        print("Inside Destructor")

    
obj = demo() 

del obj
gc.collect()


print("End of application")
