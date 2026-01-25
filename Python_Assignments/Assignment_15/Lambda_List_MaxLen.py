# write a lambda function using filter() which accepts list of strings and returns list of strings having lenght >5 

CheckStgLength = lambda Data : list(filter(lambda x: len(x)>5, Data))

def main():
    Data=list()

    No=int(input("How many strings you want in list : "))
    print("Enter the list strings : ")

    for i in range(No):
        ListStr = input(f"Enter the string {i+1} : ")
        Data.append(ListStr)

    print("Strings which length is grater then 5 are: ",CheckStgLength(Data))

if(__name__ == "__main__"):
    main()