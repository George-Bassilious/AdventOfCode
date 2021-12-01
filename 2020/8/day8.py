
def solution1():
    inputData = open('input', 'r').read().splitlines()
    stepCount=0
    acc=0

    while "vis" not in inputData[stepCount]:
        inputData[stepCount]=inputData[stepCount]+" vis"
        line=inputData[stepCount]
        line=line.split(" ")
        if line[0]=="acc":
            acc+=int(line[1][:4])
            stepCount+=1
            
        elif line[0]== "jmp":
            inputData[stepCount]=inputData[stepCount]+"vis"
            stepCount+=int(line[1][:4])
           
        elif line[0]== "nop":
            stepCount+=1
        print(stepCount)
    return acc
  
def solution2():
    inputData = open('input', 'r').read().splitlines()
    stepCount=0
    acc=0
    
    return tryPath(inputData,stepCount,acc,"")

def tryPath(inputData,stepCount,acc,change):
    print(stepCount)

    while stepCount < len(inputData):
        if "jmp +1 vis" in inputData[stepCount] :
            return acc

        if "vis" in inputData[stepCount]:
            break

        inputData[stepCount]=change+inputData[stepCount][len(change):]
        inputData[stepCount]=inputData[stepCount]+" vis"
        line=inputData[stepCount]
        line=line.split(" ")
        if line[0]=="acc":
            acc+=int(line[1][:4])
            stepCount+=1
            
        elif line[0]== "jmp":
            tryPath(inputData,stepCount,acc,"nop")
            stepCount+=int(line[1][:4])
           
        elif line[0]== "nop":
            tryPath(inputData,stepCount,acc,"jmp")
            stepCount+=1

    print(acc)
    print(stepCount>len(inputData))
    

    


    


if __name__ == '__main__':
    print(solution1())
    #print(solution2())