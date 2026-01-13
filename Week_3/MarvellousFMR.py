

def filterx(Task, Elements):
    result = list()
    for no in Elements:
        ret = Task(no)

        if(ret==True):
            result.append(no)
    return result

def mapx(Task, Elements):

    result = list()
    for no in Elements:
        ret=Task(no)
        result.append(ret)
    return result

def reducex(Task, Elements):
    sum=0

    for no in Elements:
        sum = Task(sum, no)
    return sum

