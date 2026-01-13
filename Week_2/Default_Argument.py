def EmployeeInfo(name, age, salary, city="Mumbai"):
    print("Name : ", name)
    print("Age : ", age)
    print("Salary : ", salary)
    print("City : ", city)

def main():
    EmployeeInfo("Rahul",26,2000.10) #Correct
    EmployeeInfo("Rahul",26,2000.10,"Pune") #Correct

if(__name__=="__main__"):
    main()
