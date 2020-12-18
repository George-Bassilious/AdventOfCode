with open("inn","r") as file:
   list1= file.read().splitlines()

def solution1():
    state=[".w"]
    duplicateList=[]
    list2=list1
    
    while(state != list2):
        duplicateList=[]
        for i,line in enumerate(list2):
            duplicateLine=[]
            for j,element in enumerate(line):

                if(list2[i][j]=="."):
                     duplicateLine.append(".")

                if(list2[i][j]=="L"):
                    if "".join(list(count_neighbors((i,j),list2))).count("#")==0:
                        duplicateLine.append("#")
                    else:
                        duplicateLine.append("L")

                if(list2[i][j]=="#"):

                    if "".join(list(count_neighbors((i,j),list2))).count("#")>=4:
                        duplicateLine.append("L")
                    else:
                        duplicateLine.append("#")

            duplicateList.append(duplicateLine)
        state=list2
        list2=duplicateList


    count=0
    for row in list2:
        count+=' '.join([str(a) for a in row]).count("#")
    return count



def count_neighbors(pos, matrix):
    rows = len(matrix) 
    cols = len(matrix[0]) 
   
    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
            
            if (i, j) != pos:
                yield(matrix[i][j])


def column(matrix, i):
    return [row[i] for row in matrix]

def row(matrix, j):
    return [row[i] for row in matrix]

def count_neighbors2(pos, matrix):
    (x,y)=pos
    rows = len(matrix) 
    cols = len(matrix[0]) 
    count=0
   
    count+= max(2,("".join(column(matrix,i)).count("#")))
    count+= max(2,("".join(matrix[: , y]).count("#")))

    print(count)
    return count






def solution2():
    state=[".w"]
    duplicateList=[]
    list2=list1

    '''
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.


    '''
    
    while(state != list2):
        duplicateList=[]
        for i,line in enumerate(list2):
            duplicateLine=[]
            for j,element in enumerate(line):

                if(list2[i][j]=="."):
                     duplicateLine.append(".")

                if(list2[i][j]=="L"):
                    if count_neighbors2((i,j),list2)==0:
                        duplicateLine.append("#")
                    else:
                        duplicateLine.append("L")

                if(list2[i][j]=="#"):

                    if count_neighbors2((i,j),list2)>=5:
                        duplicateLine.append("L")
                    else:
                        duplicateLine.append("#")

            duplicateList.append(duplicateLine)
        state=list2
        list2=duplicateList

    print(list2)
    count=0
    for row in list2:
        count+=' '.join([str(a) for a in row]).count("#")
    return count



if __name__ == '__main__':
    print(solution1())
    print(solution2())

