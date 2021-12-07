inputData = open('../inputs/day3', 'r').read().splitlines()

def most_frequent(List):
    return max(set(List), key = List.count)

def twos_complement(j):
   return j-(1<<(j.bit_length()))

def solution1():
    x=[]
    j=0
    for i in inputData:
        l=[(pos,char) for pos, char in enumerate(i)]
        for j in l:
            x.append(j)

    sums = [(i,list(l[1] for l in x if l[0] == i)) for i in range(0,12)]
    s=""
    for i in sums:
        s+=most_frequent(i[1])

    gamma=int(s, 2)
    epsilon= -twos_complement(gamma)
    return (gamma*epsilon)


print("Solution 1 is: ",solution1())
    


    