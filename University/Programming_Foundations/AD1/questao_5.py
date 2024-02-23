# Subprogram to find length of lists
def findLen(numLis):
    i = 0
    for item in numLis:
        i += 1
    return i


# Subprogram to search in a list if an element it's already there
def checkIfItsAlreadyInNewList(oldLis, element):
    ans = True
    for item in oldLis:
        if item == element:
            ans = False
        else:
            ans = True
    return ans


# Subprogram to find repetition in a list
def findRep(lis, lenLis):
    newList = []
    toggle = True
    i = 0
    while i < lenLis:
        j = i + 1
        while j < lenLis:
            if lis[i] == lis[j] and toggle:
                if checkIfItsAlreadyInNewList(newList, lis[j]):
                    newList += [lis[j]]
                    toggle = False
            j += 1
        toggle = True
        i += 1
    return newList


# Subprogram to print reverse lists

def printRev(lis, s):
    for i in range((s - 1), -1, -1):
        print(int(lis[i]), end=" ")


# Subprogram to count inverse numbers in a list and return the count and the new list of inversion
def countInvert(listE, siz):
    n = siz
    count = 0
    pos = []

    for i in range(n):
        for j in range(i + 1, n):
            if int(listE[i]) > int(listE[j]):
                count += 1
                pos += [(i + 1, j + 1)]

    return count, pos


# Main part of the Program

listOfNumbers = input("Type the numbers: ").split()
sizeOfList = findLen(listOfNumbers)
print("Os elementos que se repetem são: ", findRep(listOfNumbers, sizeOfList))
print("Sequência inversa:", end=" ")
printRev(listOfNumbers, sizeOfList)
countL, inversionPos = countInvert(listOfNumbers, sizeOfList)
print("Há", countL, "inversões, e as posições são:", inversionPos)
