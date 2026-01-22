import threading

icnt=0
def update():
    global icnt

    for _ in range(200000):
        icnt =icnt+1



def main():
    global icnt

    update()
    update()

    print("value of icnt is : ",icnt)


if(__name__=="__main__"):
    main()