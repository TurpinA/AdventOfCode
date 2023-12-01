import re

# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.read().strip().split('\n')
 
sum = 0

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

for line in Lines:
    dico = {}

    dico['1'] = [i.start() for i in re.finditer("1", line)]
    dico['2'] = [i.start() for i in re.finditer("2", line)]
    dico['3'] = [i.start() for i in re.finditer("3", line)]
    dico['4'] = [i.start() for i in re.finditer("4", line)]
    dico['5'] = [i.start() for i in re.finditer("5", line)]
    dico['6'] = [i.start() for i in re.finditer("6", line)]
    dico['7'] = [i.start() for i in re.finditer("7", line)]
    dico['8'] = [i.start() for i in re.finditer("8", line)]
    dico['9'] = [i.start() for i in re.finditer("9", line)]

    dico['1'] += [i.start() for i in re.finditer("one", line)]
    dico['2'] += [i.start() for i in re.finditer("two", line)]
    dico['3'] += [i.start() for i in re.finditer("three", line)]
    dico['4'] += [i.start() for i in re.finditer("four", line)]
    dico['5'] += [i.start() for i in re.finditer("five", line)]
    dico['6'] += [i.start() for i in re.finditer("six", line)]
    dico['7'] += [i.start() for i in re.finditer("seven", line)]
    dico['8'] += [i.start() for i in re.finditer("eight", line)]
    dico['9'] += [i.start() for i in re.finditer("nine", line)]

    x=[]
    for i in list(dico.values()):
        x.extend(i)

    minIndex = 0
    maxIndex = 0

    minIndex = min(x)

    if(len(x) == 1) :
        maxIndex = min(x)
    else :
        maxIndex = max(x)

    #print(f"MAX : {maxIndex}  MIN : {minIndex}")
    #print(dico)
    minV = 0
    maxV = 0

    for w in dico.items():
        if(minIndex in w[1]):
            minV = w[0]
        if(maxIndex in w[1]):
            maxV = w[0]

    print(f"First : {minV}, Last {maxV} => {int(minV + maxV)} \n")

    sum += int(minV + maxV)


    #print(list(dico.keys())[list(dico.values()).index(0)])
    # print(f"MAX : {dico.keys()[dico.get(maxIndex)]}  MIN : {get_keys_from_value(dico, minIndex)}")

print(sum)

