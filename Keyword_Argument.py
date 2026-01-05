def EmployeeInfo(name, age, salary, city):
    print("Name : ", name)
    print("Age : ", age)
    print("Salary : ", salary)
    print("City : ", city)

def main():

    # Positional call
    #EmployeeInfo("Rahul", 26, 2000.50, "pune") # Correct
    #print("")
    #print("*"*50)
    #EmployeeInfo(26,"Rahul","Pune",2000.50) # Wrong

    #Keyword call

    EmployeeInfo(age=26, name="Rahul", city="Pune", salary=2000.50) #Correct

if(__name__=="__main__"):
    main()