import threading

icnt=0
def update():
    global icnt

    for _ in range(2000000):
        icnt += 1


if(__name__=="__main__"):    
    icnt=0
    t1=threading.Thread(target=update)
    t2=threading.Thread(target=update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("value of icnt is : ",icnt)