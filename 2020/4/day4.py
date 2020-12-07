from os import replace


file1 = open('input', 'r') 
test1=file1.readlines()

fields=["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

passports=[]

def solution1():
    count=0
    temp=""
    for line in test1:
        temp+=line

        if line == "\n":
            temp= temp.replace("\n"," ").split(" ")
            passports.append(temp)
            temp=""

    temp=temp.replace("\n"," ").split(" ")
    passports.append(temp)

    for item in passports:
       count+=int(CheckValid(item))

    return count


def CheckValid(stringlist):
    str1=[]
    for input in stringlist:
        str1.append(input[:input.find(":")])

    diff=list(set(fields)-set(str1))

    return diff == [] or diff == ['cid']

       
   

if __name__ == '__main__':
    print(solution1())
    #print(solution1())
    #print(solution2())
  