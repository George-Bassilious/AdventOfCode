

inputData = open('input', 'r').read().splitlines()
boardingPasses=[]

def Calculate_seat_id(input):
    a = list(range(127+1))
    b= list(range(7+1))

    for l in input:
        if l == 'F':
           a= a[:int(len(a)/2)]
        if l == 'B':
           a= a[int(len(a)/2):]
        if l== 'R':
            b=b[int(len(b)/2):]
        if l== 'L':
            b=b[:int(len(b)/2)]
        
    input = (a[0],b[0])

    return calculate_id(input)

def calculate_id(input):
    (row,col)=input
    return (row*8)+col



def solution1():
    for boarding_pass in inputData: boardingPasses.append(Calculate_seat_id(boarding_pass))
    return max(boardingPasses)

def solution2():
    diff=list(set(range(905))-set(boardingPasses))
    return diff[-1:][0]




if __name__ == '__main__':
    print(solution1())
    print(solution2())
  