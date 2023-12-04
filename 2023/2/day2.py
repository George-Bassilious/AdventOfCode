fileName="input.txt"
inputFile = open(fileName, 'r').readlines()


inputdata =[(x.split(":")[0].replace("Game ",""),x.split(":")[1]) for x in inputFile]


def checkPossible(colorCount):
 return colorCount["red"] <=12 and colorCount["green"] <=13 and colorCount["blue"] <=14

def getMultSum(colorCount):
 return colorCount["red"] * colorCount["green"] * colorCount["blue"]

def solution1():
    totalId=0
  
    for (id,game) in inputdata:
       
        hands=game.split("; ")
        possible=True
        for hand in hands:
            rolls= hand.split(",")
            colorCount={"green":0,"blue":0,"red":0}
            for roll in rolls:
                [value,color]=roll.strip().split(" ")
                colorCount[color]+=int(value)
            if not checkPossible(colorCount):
                possible=False
                break
           
        if(possible==True):
            totalId=totalId+int(id)
           

    return totalId


def solution2():
    totalSum=0
  
    for (_,game) in inputdata:
       
        hands=game.split("; ")
        colorCount={"green":0,"blue":0,"red":0}
        for hand in hands:
            rolls= hand.split(",")
            for roll in rolls:
                [value,color]=roll.strip().split(" ")
                if(int(value)>colorCount[color]):
                    colorCount[color]=int(value)
    
        setNumber=getMultSum(colorCount)
        totalSum+=setNumber
           

    return totalSum






if __name__ == '__main__':
    print("part1: ",solution1())
    print("part2: ",solution2())