file1 = open('input', 'r') 
numbersList=[]


for line in file1.readlines():
    first = line.replace(":"," ").replace("-"," ").split()
    numbersList.append(first)



def solution1():
    count=0
    for [n1,n2,c,word] in numbersList:

        occur =word.count(c)
       
        if occur >= int(n1) and occur <= int(n2):
           # print("%s-%s"%(n1,n2))
         #   print ("%s in word : %s has count %d"%(c,word,occur))
          #  print(occur)
            count=count+1

    return count

def solution2():
    count=0
    for [n1,n2,c,word] in numbersList:

        pos1= word[int(n1)-1]
        pos2= word[int(n2)-1]

        valid1= pos1 == c and c != pos2
        valid1s= pos1 != c and c == pos2
        valid2= pos1 != c and c != pos2
        valid3= pos1 == c and c == pos2
        
       
        if valid1 or valid1s and not (valid2 and valid3):
            count=count+1

    return count


if __name__ == '__main__':
 print(solution1())
 print(solution2())