

inputData = open('input', 'r').read().splitlines() 


""" rules=[
[light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

]
 """
def solution1():
    counter=0
    used=[]
    for i in inputData:
        primary=i.split("contain")[0]
        secondary=i.split("contain")[1].split(",")
        print(primary)
        print(primary == "shiny gold bags ")
      #  print(secondary)
        matching = [s for s in secondary if "shiny gold bags" in s]
        matching2 = [s for s in primary if "shiny gold bags " in s]
        if matching !=[]:
            used.append(primary)
        if primary == "shiny gold bags ":
            counter+=1

    print(used)
    print(len(set(used)))


    return "jepp"






if __name__ == '__main__':
    print(solution1())
    #print(solution2(x))
