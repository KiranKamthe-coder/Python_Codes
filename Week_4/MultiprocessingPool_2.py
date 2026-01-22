def sumqube(no):
    sum=0
    for i in range(1,no+1):
        sum=sum+(i**3)
    return sum

def main():
    ret = sumqube(10)
    print(ret)


if(__name__=="__main__"):
    main()