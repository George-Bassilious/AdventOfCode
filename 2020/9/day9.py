import itertools


def solution1():
    with open("input") as f:
        list1= [int(f.readline()) for i in range(25)]
        n = int(f.readline())
        datae=[]+list1
        datae.append(n)

        while n in ([x+y for (x,y) in list((itertools.product(list1,repeat=2))) if x!=y]):
            list1.pop(0)
            list1.append(n)  
            
            n = int(f.readline())
            datae.append(n) 

        return datae

def solution2(data):  
    subset=subsetsum(data, data[-1])
    return min(subset)+max(subset)

#inspired from online site about pointer chasing algorithms
def subsetsum(arr,num): 
    n=len(arr)
    for i in range(n): 
        curr_sum = arr[i] 
        j = i + 1
        while j <= n:          
            if curr_sum == num: 
                return arr[i:j-1] 
      
            if curr_sum > num or j == n: 
                break
              
            curr_sum = curr_sum + arr[j] 
            j += 1
  
    print ("No subarray found") 
    return []
    

if __name__ == '__main__':
    x= solution1()
    print(x[-1])
    print(solution2(x))
