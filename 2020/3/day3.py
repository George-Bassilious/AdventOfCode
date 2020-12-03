file1 = open('input', 'r') 

test1=file1.readlines()



def solution3():
    count=0
    count2=0
    playerPos= (0,0)

    move = (3,1)
    results=[]
    for x in range(len(test1)):
        length= len(test1[1])
        print(1+x)
        print((((1+x)*3))%length)
        
        if '#' in test1[(1+x)%length][(((1+x)*3))%length]:
            count2=count2+1
       
        results.append(test1[(1+x)%length][(((1+x)*3))%length])
      

    print(len(results))

    print(count2)
    count= results.count('#')
    print(count)
   
    return count

    
    



if __name__ == '__main__':
    print(solution3())