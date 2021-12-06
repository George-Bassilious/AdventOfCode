inputdata =[(x.split(" ")[0],x.split(" ")[1]) for x in open('/mnt/c/Users/georg/Documents/hobby/AdventOfCode/2021/inputs/day2', 'r').read().splitlines()]

def solution1():
    #depths = [for number in readings.readlines()]
    moves= ['down','up','forward']
    sums = [(i,sum(int(x[1]) for x in inputdata if x[0] == i)) for i in moves]

    down = sums[0][1]
    up=sums[1][1]
    forward = sums[2][1]

    answer= (down-up)*forward
    return answer

def solution2():

    aim=0
    horizontalPos=0
    depth=0
    for (i,x) in inputdata:
       
        if i == "down":
            aim=aim+int(x)
        if i == "up":
            aim=aim-int(x)
        if i == "forward":
            horizontalPos=horizontalPos+int(x)
            depth= depth+aim*int(x)
    return depth*horizontalPos

print("Solution 1 is: ",solution1())

print("solution 2 is: ",solution2())
    

