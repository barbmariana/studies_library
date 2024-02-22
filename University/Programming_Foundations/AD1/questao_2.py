def createList():
    newList = list()
    return newList


def findSmallest(newList, qtt):
    pos = 0
    index = 0
    while index < qtt:
        if newList[pos] > newList[index]:
            pos = index
        index += 1
    return pos


def findGreatest(newList, qtt):
    pos = 0
    for item in range(qtt):
        if newList[pos] < newList[item]:
            pos = item
    return pos


def findMedia(newList, qtt):
    soma = 0
    for item in newList:
        soma += item
    m = soma / qtt
    return m


quantity = int(input("Quantos números irá inserir: "))
nList = createList()
i = 0
while i < quantity:
    nList += [int(input("Digite o número: "))]
    i += 1
smallestNumber = findSmallest(nList, quantity)
greatestNumber = findGreatest(nList, quantity)
media = findMedia(nList, quantity)
print("Menor dos", quantity, "números lidos: ", nList[smallestNumber])
print("Maior dos", quantity, "números lidos: ", nList[greatestNumber])
print("Média dos", quantity, "números lidos: ", media)
