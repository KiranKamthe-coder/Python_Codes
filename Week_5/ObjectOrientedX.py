class Arithmatic:
    def addition(self, A, B):
        return A+B

    def Substraction(self, A, B):
        return A-B


No1=0
No2=0
Ans=0

obj =Arithmatic()

No1=int(input("Enter First Number : "))
No2=int(input("Enter Second Number : "))

Ans=obj.addition(No1,No2)

print("Additon is :",Ans)

Ans=obj.Substraction(No1,No2)

print("Substraction is :",Ans)