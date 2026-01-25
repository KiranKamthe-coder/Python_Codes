class Arithmatic:
    def addition(self, A, B):
        return A+B

    def Substraction(self, A, B):
        return A-B


No1=0
No2=0
Ans=0

No1=int(input("Enter First Number : "))
No2=int(input("Enter Second Number : "))

Ans=Arithmatic().addition(No1,No2)

print("Additon is :",Ans)

Ans=Arithmatic().Substraction(No1,No2)

print("Substraction is :",Ans)