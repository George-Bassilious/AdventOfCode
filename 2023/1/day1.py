fileInput = open('input.txt', 'r').readlines()

def solution1():
    total=0
    for line in fileInput:
        first_digit,last_digit=getDigits(line)
        z = int(str(first_digit)+str(last_digit))
        total=total+z

    return total

def solution2():
    total2=0
    for line in fileInput:
        first_digit,last_digit=getDigits(parseText(line))
        z = int(str(first_digit)+str(last_digit))
        total2=total2+z

    return total2

def getDigits(line):
    first=0
    last=0
    for character in line:
        if(character.isdigit()):
            first=character
            break
    for character in line[::-1]:
        if(character.isdigit()):
            last=character
            break

    return first,last

def parseText(line):
    numbers=["one","two","three","four","five","six","seven","eight","nine"]
    for number in numbers:
        if line.find(number) != -1:
          line=line.replace(number,number[0]+str(numbers.index(number)+1)+number[len(number)-1])
    return line




if __name__ == '__main__':
    print("part1: ",solution1())
    print("part2: ",solution2())