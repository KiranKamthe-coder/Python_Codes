from MarvellousFMR import filterx, mapx, reducex

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No+1
Add = lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ", Data)

    FData = list(filterx(CheckEven, Data))
    print("Data after filter is : ", FData)

    MData = list(mapx(Increment, FData))
    print("Data after map is : ",MData)

    RData = reducex(Add, MData)
    print("Data after reduce is : ", RData)
    
if (__name__=="__main__"):
    main()
