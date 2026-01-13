from functools import reduce


CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No+1
Add = lambda A,B : A+B

def filterx(Task, Elements):
    result = list()
    for no in Elements:
        ret = Task(no)

        if(ret==True):
            result.append(no)
    return result


def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ", Data)

    FData = list(filterx(CheckEven, Data))
    print("Data after filter is : ", FData)

    MData = list(map(Increment, FData))
    print("Data after map is : ",MData)

    RData = reduce(Add, MData)
    print("Data after reduce is : ", RData)
    
if (__name__=="__main__"):
    main()
