# Function to save the names into a dict that will have the name : numbers
def save_names(file_path):
    new_dict = dict()
    try:
        file_p = open(file_path, "r")
        try:
            for line in file_p:
                name, *numbers = line.split("#")
                new_dict[name] = []
                for num in numbers:
                    new_dict[name].append(int(num))
        except FileExistsError:
            print("Erro ao ler arquivo")
            pass
        file_p.close()

    except FileNotFoundError:
        print("Erro ao buscar arquivo")
        pass

    return new_dict


# Function to open a file and read
def read_content(file_path):
    file = open(file_path, "r")
    if file.readline() == "":
        file.close()
        print("Nenhuma Aposta!!")
        return
    print("Conteúdo do Arquivo de Apostas Teste2:")
    for line in file:
        print(line, end="")
    print("------ Fim do Arquivo de Apostas ------")
    file.close()
    return None


# Function to convert arr of strs to nums
def convert_str_num(arr):
    arr = arr.strip().split(" ")
    i = 0
    while i < len(arr):
        arr[i] = int(arr[i])
        i += 1
    return arr


# Function to create a dictionary that archive the winner numbers and the people that won
def calculate_corrects_numbers(people, numbers):
    d = dict()
    for person in people:
        counter = 0
        for num in numbers:
            if people[person].count(num):
                counter += 1

        if d.get(counter) is None:
            d[counter] = set()
        d[counter].add(person)

    return d


# Function to print the answers
def print_answer(dict):
    total_winners = 0
    for i in range(3, 9):
        if i in dict:
            total_winners += len(dict[i])
    if total_winners == 0:
        print("ACUMULOU TUDO")
        return None
    for i in range(8, 2, -1):
        if dict.get(i) is not None:
            print("Foi(ram)", len(dict[i]), "Ganhador(es) com", i, "Acertos:")
            sort_and_print(list(dict.get(i)))
        elif dict.get(i) is None:
            print("Ninguém acertou", i, "Números !!")


# Function to sort the names and print them
def sort_and_print(names):
    for i in range(len(names) - 1):
        for j in range(len(names) - i - 1):
            if names[j] > names[j + 1]:
                aux = names[j]
                names[j] = names[j + 1]
                names[j + 1] = aux
    for name in names:
        print(name)
    return


# Program
file = input("Digite o arquivo de texto desejado: ")
read_content(file)
new_dictionary = save_names(file)
nums = input("Digite os números sorteados: ")
nums = convert_str_num(nums)
print("Total de Apostas:", len(new_dictionary))
final_dic = calculate_corrects_numbers(new_dictionary, nums)
print_answer(final_dic)
