file1 = open('inputs/day1', 'r') 
numbersList = list(map(int, file1.readlines()))

def solution1():
    count=-1
    mem=-1
    for i in numbersList:
        if i > mem:
            count=count+1
        mem= i

    print("Answer 1: ", count)

def solution2():
    count=-1
    mem=-1
    for i,val in enumerate(numbersList,-3):
        var=val+numbersList[i+1]+numbersList[i+2]
        if  var > mem:
            count=count+1
        mem = var

    print("Answer 2: ", count)

solution1()
solution2()

#This code was taken from https://github.com/IanFindlay/advent-of-code/blob/master/2021/day_01.py
def idealSolution ():
    with open('inputs/day1', 'r') as readings:
        depths = [int(number.strip()) for number in readings.readlines()]

        increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]])

        # Answer One
        print("Number of times the depth increases:", increased)

        increased = sum([1 for i in range(3, len(depths)) if depths[i] > depths[i-3]])
        # Answer Two
        print("Number of times the sliding window increases:", increased)

idealSolution()