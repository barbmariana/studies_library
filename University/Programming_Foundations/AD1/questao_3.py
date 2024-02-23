def printBigger(nList, lastNum, listSize):
    for index in range(0, listSize):
        if float(nList[index]) > float(lastNum):
            print(nList[index])


entry = input("Type a number: ")
newList = []
i = 0

while entry != '':
    float(entry)
    newList += [entry]
    i += 1
    entry = input("Type a number: ")

print("Relação dos Números Maiores que", newList[-1], ":")
listLen = i
printBigger(newList, newList[-1], listLen)
