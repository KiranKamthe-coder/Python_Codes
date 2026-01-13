Value1=[10,20,30,40,10]  #list allow , ordered so it has index , start with 0
Value2=(10,20,30,40,10)  #Tuple allow duplicate,ordered so it has index ,start with 0
Value3={10,20,30,40,10}  #Set not allowed duplicate, not ordered so it has no index

print(Value1[0])    #10
print(Value2[0])    #10
#print(Value3[0])   #error

Value1[2]=35        #Can change value as it is mutable
#Value2[2]=35       #error can't change value as its immutable
print(Value1[2])
#print(Value2[2])

