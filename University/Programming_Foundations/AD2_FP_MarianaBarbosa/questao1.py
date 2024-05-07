# Function to read numbers
def read_arr(arr):
    for num in arr:
        print(num, end=" ")
    return


# Function to save numbers into a list
def save_num(file_path):
    new_arr = []
    try:
        file = open(file_path, "r")
        try:
            for line in file:
                numbers = line.split()
                for n in numbers:
                    try:
                        float_n = float(n)
                        new_arr.append(float_n)
                    except ValueError:
                        print("Número não é do tipo float")
                        pass
        except FileExistsError:
            print("Erro ao ler arquivo")
            pass
        file.close()

    except FileNotFoundError:
        print("Erro ao buscar arquivo")
        pass

    return new_arr


# Function used to calculate the media of the numbers
def calculate_media(arr):
    total_sum = 0
    try:
        for item in arr:
            total_sum += item
    except ZeroDivisionError:
        print("Divisão por zero não permitida")
        pass
    return total_sum / len(arr)


# Function to calculate quantity above media
def calculate_above(arr, media):
    i = 0
    qtt = 0
    while i < len(arr):
        if arr[i] > media:
            qtt += 1
        i += 1
    return qtt


# Functions used to ordinate elements using Selection Sort
def the_smallest(arr, pos):
    i = pos + 1
    pivot = pos
    while i < len(arr):
        if arr[i] < arr[pivot]:
            pivot = i
        i += 1

    return pivot


def selection_sort(arr):
    i = 0
    while i < len(arr):
        smallest = the_smallest(arr, i)
        aux = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = aux
        i += 1
    return arr


# Program
arc_name = "inputAD2.txt"
print("Conteúdo em %s:" % arc_name)
# Create new List and print numbers
new_arr = save_num(arc_name)
read_arr(new_arr)
print("\n", end="")
# Print the media
media = calculate_media(new_arr)
print("Média dos Números em {}: {}".format(arc_name, media))
# Print quantity above the media
quantity_above = calculate_above(new_arr, media)
print("Quantidade Acima de {} em {}:{}".format(media, arc_name, quantity_above))
# Print sorted array
sorted_array = selection_sort(new_arr)
print("Ordem Crescente:", end="")
read_arr(sorted_array)
