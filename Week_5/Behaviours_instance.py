class demo:
    No=10

    def __init__(self,A,B):
        self.value1=A
        self.value2=B
        
    def fun(self):
        print("inside instance method fun ",self.value1,self.value2)

    @classmethod
    def sun(cls):
        print("Inside class method sun",cls.No)


demo.sun()
print("class variable No :",demo.No)

obj =demo(11,21)

obj.fun()
print("Instance variable ",obj.value1, obj.value2)