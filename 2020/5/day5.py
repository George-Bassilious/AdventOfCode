

text = open('input', 'r').read().splitlines()

boardingPasses=[]

def tester(input):
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

    return input


def solution2():
    diff=list(set(range(905))-set(boardingPasses))
    return diff[-1:][0]




def solution1():
    max_seat_id=0
    
    for boarding_pass in text:
        
        x= calculate_seat_id(tester(boarding_pass))
        boardingPasses.append(x)

        if  x > max_seat_id:
            max_seat_id= x

    return max_seat_id

def calculate_seat_id(input):
    (row,col)=input
    return (row*8)+col

if __name__ == '__main__':
    print(solution1())
    print(solution2())
  