
inputData = open('input', 'r').read().splitlines() 
Groups=[]

def readInput():
    tempgroup=[]
   
    for i in inputData:
        if i == "":
            Groups.append(tempgroup)
            tempgroup=[]
        else:

           tempgroup.append(i)
       
    Groups.append(tempgroup)




def solution1():
    readInput()
    sum=0
    for i in Groups:sum+=len((set("".join(set(i)))))
    return sum

def solution2():
    sum=0  
    for i in Groups:

        temp=set(i[0])
        for s in i:

            temp=set(s) & temp

        sum+=len(temp)
    return sum



if __name__ == '__main__':
    print(solution1())
    print(solution2())