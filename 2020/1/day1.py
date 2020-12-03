file1 = open('input', 'r') 
numbersList = set(map(int, file1.readlines()))

def solution1():
    for number in numbersList:
        x=(2020-number)
        if x in numbersList:
            return x*number

def solution2():
     for number in numbersList:
         for number2 in numbersList:
            x=(2020-number-number2)
            if x in numbersList:
                return x*number*number2





if __name__ == '__main__':
    print(solution1())
    print(solution2())