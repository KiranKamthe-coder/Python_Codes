# write a lambda function using filter() which accepts list of number and returns list of numbers which are divisble by
# 3 and 5 both

CheckDivisible = lambda Data : list(filter(lambda x: (x%3==0 and x%5==0), Data))

def main():
    Data=list()

    No=int(input("How many numbers you want in list : "))
    print("Enter the list numbers : ")

    for i in range(No):
        ListNo = int(input(f"Enter the string {i+1} : "))
        Data.append(ListNo)

    print("Numbers which are divisible by 3 and 5 are : ",CheckDivisible(Data))

if(__name__ == "__main__"):
    main()