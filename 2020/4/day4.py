import string

file1 = open('./inputs/input', 'r') 
test1=file1.readlines()

fields=["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

passports=[]

requirements = [
    ['byr',lambda num: 1920 <= int(num) <= 2020],
    ['iyr',lambda num: 2010 <= int(num) <= 2020],
    ['eyr',lambda num: 2020 <= int(num) <=2030],
    ['hgt',lambda num:  (num[-2:]=='in' and 59 <=int(num[:-2]) <=76) or (num[-2:]=='cm' and 150 <=int(num[:-2]) <=193) ],
    ['ecl',lambda string: string in ["amb","blu","brn","gry","grn","hzl","oth"]],
    ['pid',lambda input: len(input)==9 and input.isdigit()],
    ['hcl',lambda string1: string1[0]=="#" and len([x for x in ''.join(string1[1:]) if x not in string.hexdigits])==0]
]


def find_all_valid(special):
    passports=[]
    temp=""
    for line in test1:
        temp+=line

        if line == "\n":
            temp=temp.replace("\n"," ").split(" ")

            if(CheckValid(temp)):
                passports.append(temp)
            temp=""

    #Bara för sista fallet, kan tas bort men då måste man dubellkolla sista passet!
    temp=temp.replace("\n"," ").split(" ")
    if CheckValid(temp):
        passports.append(temp)
       

    if special:
        passport2=[]
        for passport in passports: 
            bool = 1
            for input in passport:
                for i in requirements:
                   
                    if input.split(":")[0] in i:
                        if not i[1](input.split(":")[1]):
                            bool=0
                        break
                if not bool:
                    break
    
            if(bool):
                passport2.append(passport)   
        

        return  passport2
      
    return passports

def CheckValid(stringlist):
    str1=[]
    for input in stringlist:
        str1.append(input[:input.find(":")])

    diff=list(set(fields)-set(str1))

    return diff == [] or diff == ['cid']


def solution1():
    return len(find_all_valid(0))

def solution2():
    list= find_all_valid(1)
    return len(list)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
  