file1 = open('input', 'r') 
test1=file1.readlines()


def treeFinder(x,y):
    count=0
    playerpos=y
    length= len(test1[0])-1
    for line in range(x,len(test1),x):
    
        if '#' in test1[line][(playerpos%length)]:
            count=count+1
        playerpos= playerpos+y

    return count



def solution1():
    return treeFinder(1,3)

def solution2():
    count=1
    slopes=[(1,1),(1,3),(1,5),(1,7),(2,1)]
    for (x,y) in slopes:
        count*= treeFinder(x,y)
    
    return count

if __name__ == '__main__':
    print(solution1())
    print(solution2())
  