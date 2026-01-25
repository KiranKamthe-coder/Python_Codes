class demo:
    No=10

    def __init__(self,A,B):
        self.value1=A
        self.value2=B
        
print("Class variable No : ",demo.No)

obj1=demo(11,21)
obj2=demo(51,101)

#print(obj1.No) Allowed
#print(obj2.No) Allowed

print("Instance variable of obj1: ",obj1.value1, obj1.value2) # 11 21
print("Instance variable of obj2: ",obj2.value1, obj2.value2) # 51 101

obj1.value1=15
demo.No=0


print("Instance variable of obj1: ",obj1.value1, obj1.value2) #15 21
print("Instance variable of obj2: ",obj2.value1, obj2.value2) # 51 101

print(demo.No) # 0 
