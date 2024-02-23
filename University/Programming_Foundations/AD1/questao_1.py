# Make letters upperCase
def upperCase(str_element):
    if 97 <= ord(str_element) <= 122:
        return chr(ord(str_element) - 32)
    return str_element


# Make letters lowerCase
def lowerCase(str_element):
    if 65 <= ord(str_element) <= 90:
        return chr(ord(str_element) + 32)
    return str_element


# Main Program
letter = input("Type a letter: ")
phrase = input("Type the phrase: ")
letterLower = lowerCase(letter)

words = 0
while phrase != '':
    printOrNot = False
    newList = phrase.split(" ")
    for word in newList:
        if word[0] == letter or word[-1] == letter or word[0] == letterLower or word[-1] == letterLower:
            printOrNot = True
        if printOrNot:
            for let in word:
                let = upperCase(let)
                print(let, end="")
            words = words + 1
            print(" ")
        printOrNot = False

    printOrNot = False
    phrase = input("Type the phrase: ")

print("Iniciadas ou Finalizadas pelo Caracter", letter, "=", words, "vez(es)")
