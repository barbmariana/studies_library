vert = input()
tipo = input()
alim = input()
res = ["aguia", "pomba", "homem", "vaca", "pulga", "lagarta", "sanguessuga", "minhoca"]

if vert == "vertebrado":
    if tipo == "ave" and alim == "onivoro":
        print(res[1])
    elif tipo == "ave" and alim == "carnivoro":
        print(res[0])
    elif tipo == "mamifero" and alim == "onivoro":
        print(res[2])
    elif tipo == "mamifero" and alim == "herbivoro":
        print(res[3])
else:
    if tipo == "inseto":
        if alim == "hematofago":
            print(res[4])
        else:
            print(res[5])
    else:
        if alim == "hematofago":
            print(res[6])
        else:
            print(res[7])
