from random import randint


def arch_points(nam, qtd, min, max):
    arq = open(nam, "w")
    for pos in range(qtd):
        arq.write(str(randint(min, max)) + " " + str(randint(min, max)) + "\n")

    arq.close()
    return None


def show(nam):
    arq = open(nam, "r")
    for pt in arq:
        print(pt, end="")
    arq.close()
    return None

arch_points("pontos.txt", 30, 0, 400)
show("pontos.txt")