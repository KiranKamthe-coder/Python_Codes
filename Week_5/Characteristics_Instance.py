import gc

class demo:
    # Class Variable
    No1=10 #class variables 
    No2=11 #class variable

    def __init__(self):

        # instance variable
        self.A=101
        self.B=201
        print("inside constructor")

    def __del__(self):

        print("Inside Destructor")

print(demo.No1)
print(demo.No2)

obj = demo()

print(obj.A)
print(obj.B)