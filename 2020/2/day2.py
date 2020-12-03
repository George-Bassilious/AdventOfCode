file1 = open('input', 'r') 
numbersList=[]


for line in file1.readlines():
    first = line.replace(":"," ").replace("-"," ").split()
    numbersList.append(first)



def solution1():
    count=0
    for [n1,n2,c,word] in numbersList:
        diff=abs(int(n2)-int(n1))
        occur =word.count(c)
        if occur > int(n1) and occur < int(n2):
            count=count+1
    

        
    return count
       # print(string,string2,string3[0])




if __name__ == '__main__':
 print(solution1())