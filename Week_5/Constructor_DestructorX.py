import gc

class demo:
    def __init__(self):
        print("inside constructor")

    def __del__(self):
        print("Inside Destructor")

#use   
obj1= demo()
obj2= demo() 

#deallocate
del obj1
del obj2

gc.collect()


print("End of application")
