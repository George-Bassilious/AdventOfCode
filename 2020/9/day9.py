import itertools


def solution1():
    with open("input") as f:
        list1= [int(f.readline()) for i in range(25)]
        n = int(f.readline())
        
        while n in ([x+y for (x,y) in list((itertools.product(list1,repeat=2))) if x!=y]):
            list1.pop(0)
            list1.append(n)   
            n = int(f.readline())

        return n


if __name__ == '__main__':
    print(solution1())
    #print(solution2())

    