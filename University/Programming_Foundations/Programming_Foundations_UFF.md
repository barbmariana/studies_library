# Programming Foundations 

## A programação

É composta por:

- Estrutura de dados: Forma como armazenamos informaçoes e dados em computador

- Algoritmo : Descrição de padrão de comportamento

Programa = Algorimo + Estrutura de Dados

## Paradigma de Programação Estruturada:

- Facilitar desenvolvimento de programas
- Facilitar a leitura (entendimento dos programas)
- Permitir a validação a priori dos programas
- Facilitar a manutenção e modificação dos programas

## Ciclo de vida do software

1 - Especificar os requisitos do problema - Preparar uma especificação completa e não ambígua
2 - Analisar o Problema - Entende problema, avalia soluções e escolhe soluções
3 - Projetar o programa para solucionar problema - Fazer projeto de cima pra baixo (top down), Para cada módulo identificar as princiipais estruturas e subprogramas, desenvolver algoritmos e estruturas de dados
4 - Implementar o Projeto - Codificar a solução, corrigir erros de codificação
5 - Testar e Validar o programa - Testar o código e validá-lo
6 - Manter e atualizar - Executar sistema, avaliar seu desempenho, remover erros posteriores, realizar modificações e atualizar

## Python

Criada na década de 80, por Guido Van Rossum

É multiparadima, interpretada, tem sua tipagem dinâmica, é multiplataforma podendo ser executada em diferentes SO, gerencia a sua própria memória. 

IDE --> Pycharm

## Correção de exercícios

- Teste de Mesa - validação do programa em papel, representa graficamente suas variáveis e acompanhe a atualização dos valores
- Juiz remoto - Sistema web que compila e executa código fonte submetido

## Variáveis

Área de memória que mantém valor que pode ser mudado. 

Tem seu identificador que é iniciado por letra minúscula

Padrão: Camel case, apenas caracteres alfa-numéricos

## Tipos básicos

Tipos embutidos, são imutáveis

- Tipos integrais 
        - Inteiro (int): Podem ser centenas de dígitos, limitado pela memória do pc. 
        - Lógico (bool) :  0 é False e 1 é true
        - Flutuante(float)
        - String (str) - sequencia caracteres

Comandos de Conversão:
int, float, bool, str

ex:
a = int(input())
b = int(input())
x = a + b
print(x)

## Comandos de atribuição

Comando mais importante de uma linguagem imperativa

Em um comando de atribuição, variável recebe resultado de avaliação de expressão.

## Linguagem de tipagem dinâmica

A tipagem é dinâmica e muda de acordo com a atribuição. As atribuições funcionam como referência para uma área de memória que reserva o espaço para aquele tipo.

## Operadores unários

Operador de positivo e negativo, aceita um operando só.
Exemplo:
-a ou -15

Operador lógico de Não !

## Operadores Binários

Aceitam dois operandos. Como o + - x / //(divisão inteira) %(resto) *(potenciação)

## Operadores binários lógicos

&& AND
|| OR
== != 
>= <= > <

## Precedência

()
Potenciação
Unários
Binários multiplicativos
Binários aditivos
Relacionais
Lógico not
Lógico and
Lógico or

## Comandos de saída padrão

print() - > escreve na saída padrão a expressão. No final pula pra próxima linha. 

podemos usar o atributo end= para colocar uma expressão de término

- As expressões podem ser formatadas. Colocamos % e depois o tipo do formato. d(inteiro), f(float), s(string).

print("%f + %f" %(157.8313, 3.5), end = "!!!")

## Comandos de entrada padrão

input()

- Comando que aguarda o usuário fornecer pela entrada padrão, o teclado. Este comando tem o efeito de suspender a execução até que o usuário escreva.

aluno = input("digite o nome: ");


difs = str((a * b) - (c * d))
print("DIFERENCA =", difs)

ou

print("DIFERENCA = " + difs)

ou

difs = (a * b) - (c * d)
print("DIFERENCA = %d" %difs)

ou

print("A soma =', soma, "e o Produto =', prod)
print("NUMBER =", eNumber, "SALARY =", totalSalary)


## Sequência de Comandos

Em python construímos a sequência de comandos um por linha, um abaixo do outro, mantendo todos na mesma indentação

- Suite é um bloco de comandos
- Comentários são iniciados com o caractere # 
- Comentários de múltiplas linhas ficam entre ''' '''. 

## Estrutura de seleção com um ramo (if)

A estrutura de seleção com ramo if é utilizada quando se deseja executar comando ou suite apenas em uma condição

if <condicao>:
        <execucao>


## Estrutura de seleção composta

if(valor >= 10) and (valor <=20):
        print...
if 10<= valor <=20:
if (valor < 0) or (valor > 30):
        print...

### Estrutura seleção com dois ramos

if <condicao>:
        ...
else:
        ...

### Estrutura de seleção aninhadas

if <condicao> :
        ...
elif <condicao>:
        ...
else:
        ...

## Split
Divide a string, considerando o espaço em branco como separador, em uma lista de substrings

valores = input("Entre com dois números:").split()
x = int(valores[0])
y = int(valores[1])

## None

É o tipo nenhum. Ele denota falta de valor.

## Estrutura de repetição indefinida (WHILE)
Utilizamos mais quando queremos utilizar comandos em vezes inderteminadas. Então colocamos uma expressão que deverá ser executada enquanto a condição for verdadeira.

while <condicao>:
        <suite>

ex:
num = int(input("fale um numero: "))
i = 1
fat = 1
while i <=num:
        fat = fat * i
        i = 1 + 1
print(fat)

## Estrutura de repetição definida (FOR)
É utilizada quando sabemos os números de repetições

for <var> in <list>:
        <suite>
A cada repetição, var assume o valor do item

for item in {3, 4, 5, 6}:
        print(item, end=" ")
print()  //aqui ele pula a última linha

## Range

- Para criar uma lista com uma progressão aritmética de elementos, podemos utilizar range

- range(valor limite) - Cria uma lista com progressão dos itens de razão 1 iniciada no zero até o limite, lembrando que ele segue até o valor que antecede o limite. 

- Sempre vai até valores que antecedem limites

ex : 
range(5) [0, 1, 2, 3, 4]

range(valor inicial, valor limite)
ex:
range(8, 13) [8, 9, 10, 11, 12]

range (valor inicial, valor limite, avanço)
ex:
range(1, 7, 2) [1, 3, 5]
range(5, -14, -3) [5, 2, -1, -4, -7, -10, -13]

num = int(input("digite um num"))
fat = 1
for i in range(1, num+1):
        fat = fat * i


## Subprogramação :  Funções

- permite que diferentes partes do programa possam ser desenvolvidas e testadas separadamente

- trata-se de grupos de sentenças, suite, comando de controles ao qual é atribuido nome e retorna valor

def nomeFunção(lista de parametros):
        suite do corpo da função

A suite pode ter zero ou mais retornos de valores, se não tiver valor podemos botar return ; ou return none

- Elas devem ser declaradas antes de serem utilziadas, portanto deve ficar acima do prorama principal.

def mult(x, y):
        z = 0
        for u in range(x):
                z = z + y
        return z;

- No início da função os parametros sempre são inicializados com cópia de referencias(ponteiros) para os valores passados na ativação da função

- os valores podem vir de constantes, variáveis, resultados de funções

def trocar(valores, pos1, pos2):
        if 0 <= pos1 < len(valores) and 0 <= pos2 < len(valores):
                temp = valores[pos1]
                valores[pos1] = valores[pos2]
                valores[pos2] = temp
        return None;

- A passagem de parametro ocorre como se o primeiro argumento substituisse o parametro dentro do escopo da função

- Não precisamos retornar nada porque a função é uma função de ação, ela realiza apenas a troca

- Podemos fazer funções com funções como parâmetros

def soma(f, n):
        parcial = 0
        for in in range(1, n + 1):
                parcial = parcial+f(ind)
        return parcial

## Escopo de identificador em Python

- Parâmetros de variáveis locais e as funções declaradas internamente a uma função definem identificadores que são locais a esta função, isto é: tem escopo local

- Estes identificadores não podem ser utilizados fora da respectiva função, isto é, não são visíveis em outra parte do programa

- identificador é chamado global se nomeamos como global e tem o mesmo valor no programa inteiro
- identificador local só vale dentro de subprogramas e blocos

- variáveis globais podem ser visualizadas dentro de subprogramas mas não podem ser alteradas nos mesmos

- se tivermos a mesma variavel como global e como local, a que passa a valer é a mais local. 

z**3 é ao cubo

## Rescursividade

- uma função possui no seu corpo uma chamada de si própria
- É uma repetição mas sem estruturas de repetição
- exemplo fatorial:

de fat(n):
        if n >= 1:
                return 1;
        else
                return n * fat(n - 1)

- exemplo iterativo

def fat(n):
        p = 1
        for i in range(1, n+1)
                p = p * i
        return p;

## Estrutura de dados

- Vetor: Agregado de elementos de mesmo tipo em python. É uma lista sequencial. Estrutura homogênea, todos elementos igualmente acessíveis. Vator [].
        - itens[0] - primeira posição
        - itens [i - 1]
        - Podemos ler todos os itens de uma vez e usar o split para separar os elementos. 

        Duas formas de percorrer vetor:

        soma = 0
        for indice in range(0, 100):
                soma = soma + itens[indice]

        ou

        for item in itens:
                soma = soma + item

        for index in range(len(itens))
                soma = soma + itens[indice]

        - valores = [None]*10
        - Para adicionar itens em lista podemos usar o .append()

- Matriz: Vetores de dupla dimensão
        - São vetores de vetores
        - Podemos chamar-los com [][]
        ex:
        resposta =[]
        for inAluno in range(qtdAlunos):
                nome = input(difite o nome: )
                linha = [nome, []]
- String :  Cadeia de caracters, str
        - Representa cadeia de caracteres de tamanho e valor imutável
        - Pode ser iniciado ou finalizado com "" ou ''
        - len(string) = tamanho
        - Podemos utilizar comparadores relacionais e eles irão comparar letra por letra; 
        - Indexação de caracter é igual o vetor
        - Podemos concatenar com +
        - Fatiamento: nomeString[posiçãoinicial : posicaofinal + 1] -> uma nova sub string
        ex:
        nome "Julia Rocha"
        sobrenome = nome[6:len(nome) - 1]
        - Método find(substringProcurada). se não encontrar retorna -1. Pode ter substringProcurada, posicaoInicio e posição fim como argumentos
        - replace(substringProcurada, novastring) - retorna copia da string sendo consultada com a substituicao
        - count(substringprocurada) - retorna quantidade de ocorrencias da substring procurada na string
        - upper -  copia da string letra maiuscula
        - lower -  copia da string letra minuscula
        - strip - retorna copia da string removendo todos eventuais caractereis no inicio e fim
        - split - retorna uma lista de todas as palovras
        - split(unidadeSeparadora)
- Tupla : sequencia ordenada de zero ou mais referencias a objetos. Suportam mesmo fatiamento, mesmo acesso e desempacotamento de vetores e strings.
        - Pode ser vazia
        - (valor, )
        - Valor pode ser de qualquer tipo
        vazio = tuple() ou vazio = ()
        - nPode ter  valores de diferentes tipos
        - Vetores e strings podem ser empacotados como tuplas atravez da função tuple
        trio = tuple([1, 2 ,3]) tuple("aeiou") = ("a", "e", "i", "o", "u")
        - podemos fazer desestruturação, ou desacoplamento
        (nome, idade) = ("Maria", 30)
        - Podemos usar for para iterar
        - count(valor) - retorna quantidade de ocorrencias
        - index(valor) - retorna index da primeira ocorrencia de determinado valor
        - concatenação - Gera nova dupla da primeira com a segunda
        - replicação - a * n, gera uma nova dupla a partir do conteudo da primeira repetido n - 1 vezes
        - fatiamento = a[posicaoinicial: posiçãofinal + 1]
        - teste in ou not in - verifica a pertinencia de determinado valor




## Organizando programas:

- Primeiro pense nos inputs e outputs
- Pense em todos subprogramas e necessidades que temos
- Crie os def e seus argumentos e vetores

## Algoritmos de Busca

Se utilizarmos algoritmo simples com for nossa complexidade será O(n), ou seja, não é muito eficiente. Podemos colocar o return no mesmo momento que achamos para não precisar rodar o laço inteiro.

- Busca com sentinela : O algoritmo usa menos  comparações, se não precisar andar até o final. Inserimos um elemento a mais no final do vetor.O elemento será encontrado, mas se a posição for n + 1 ele não pertence ao vetor. de vez rodar o laço com i < len usamos vetor[in] != elementoprocurado

- Busca binária: Os n elementos devem estar ordenados e também sem repetição. Vamos sempre pegar o inicio e fim e dividir // por dois, para termos a divisão inteira. Depois rodamos a partir da proxima metade

def buscaElemento
(arr, procurado):

inicio = 0
fim = len(arr) - 1

meio = (inicio + fim) // 2

while (inicio < fim) and procurado != arr[meio]:
        if(procurado > arr[meio]):
                inicio = meio + 1
        else:
                fim = meio - 1
        meio = (inicio + fim) // 2
if(procurado != valores[meio])
        local = -1
else:
        local = meio
return local

## Moda

Moda de um vetor é o elemento que aparece com mais frequencia. O problema de busca pela moda consiste em encontrar esse elemento no vetor . 
Precisamos ou de um vetor e um outro auxiliar que contém a frequencia dos elementos. Teremos a primeira posição do numero mais frequente

def preenche(valores):
        for ind in range(len(valores)):
          valores[ind] = int(input)
        return None
def buscaModa(valores):
        auxiliar = [0] *len(valores)
        for indice in range(len(valores)):
                for i in range(indice + 1, len(valores)):
                        if(valores[i] == valores[index]):
                        auxiliar[indice] += 1
        posModa = 0
        for i in range(1, len(auxiliar)):
                if( auxiliar[i] > auxiliar[posModa]):
                        posModa = i
        return pos moda

- Busca pela Moda de vetor ordenado:

def buscaModa(valores):
        moda = valores[0]
        ind = 0
        frequencia = 1
        while ind < len(valores) - 1:
                ind = ind + 1
                if(valores[ind] == valores[ind - frequencia]):
                        moda = valores[ind]
                        frequencia = frequencia + 1
        return moda

## Ordenação

- organização de conjunto de elemento do mesmo tipo
- sem perda de generalidade o problema será atacado considerando-se que : os elementos a serem ordenados são numéricos e estão armazenados em vetor

- Selection Sort : para cada posição i do vetor valores o algoritmo procura pelo menor elemento e coloca na posição i

``
def buscaMenor(arr, pos):
        i = pos
        pivot = pos
        while (i < len(arr)):
                if(arr[i] < arr[pivot]):
                        pivot = i
                i += 1
        return pivot

def ordena(arr):

        i = 0
        aux = 0
        while (i < len(arr)):
                menor = buscaMenor(arr, i)
                aux = arr[i]
                arr[i] = arr[menor]
                arr[menor] = aux
                i += 1

        return arr

arr = [1, 23, 21, 11, 43, 2, 3, 4, 65, 1, 2, 3, 2, 4, 0, 78]
print(ordena(arr))
``

- Método da bolha 

executa n - 1 iterações na parte mais externa. Percorre todo array na parte mais interna

A cada laço externo teremos uma posição correta

``
def ordena(valores):
        n = len(valores)
        for i in range(n - 1):
                #aqui não preciso repetir até o final porque o j irá fazer essa comparação para gente
                for j in range(0, n - 1 - i):
                        #aqui vamos ir andando sempre menos i porque ele tb será o contador de quantos já corrigimos
                        if(valores[j] > valores[j + 1]):
                                aux = valores[j]
                                valores[j] = valores[j + 1]
                                valores[j + 1] = aux
        return valores
arr = [1, 3, 2, 4, 8, 22, 3, 44, 3, 32, 12, 10]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

        #  Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
``

- Ordenação Pelo Método de Partição ( QUICKSORT)

        - um elemento do vetor é escolhido e denominado pivot
        - todos os elementos do vetor sao rearrumados ocupando as primeiras celulas do vetor os elementos menores que o pivo
        - inicio = 0 final = len(valores)
        - i = inicio + 1
        - final = j
        - i só é incrementado se ele for maior que o pivot

        - 1º Escolher o pivot
        - 2º Duas partições são criadas, esquerda e direita. A esquerda ficam o menor (A[i]) ou igual ao pivot e direita (A[j]) o maior ou igual
        - O melhor caso é quando o pivot está literalmente no meio


``

def get_words():
        fname = "caminho arquivo"
        wordlist = []
        with open(fname, "r") as fd:
                for line in fd:
                        wordlist.append(line.strip())
        return wordlist

def     quick_sort(arr, low, up):
        if low < up:
                pivot = partition(arr, low, up)
                quick_sort(arr, low, pivot - 1)
                quick_sort(arr, pivot, up)

def partition(arr, low, up):
        center = (low + up) //2
        pivot = arr[ low + center]

        i = low
        j = up
        while True:
                while arr[i] < pivot:
                        i = i + 1
                while arr[j] > pivot:
                        j = j + 1
                if i >= j:
                        return j
                aux = arr[i]
                arr [i] = arr[j]
                arr[j] = aux
                




``


## Listas
- É uma sequencia ordenada pelo indice, de zero ou mais referencias a objetos
- É uma estrutura de dado recursiva. Quando tem zero elementos é representada pelo []. Quando tem um ou mais elementos é representada por sequencia e colchetes. 
- Se for vazia é representada : []
- São mutáveis, podendo receber ou terem elementos removidos
- Cada item temos um valor e também uma referencia para o próximo

- append(novoElemento) - anexa novoElemento no fim da lista
- insert(pos, novoElemento) - insere novo elemento na pos da lista. 

Exemplo:

def preencher(listaelementos, qtd, min, max):
        from random import randint
        for item in range(qtd):
                listaelements.append(randint(min, max))
        return None

- pop() - retorna e remove o último elemento da lista, o mais a direita. Se ela tiver vazia vai dar um erro
- pop(pos) - retorna e remove item na posição pos
- remove(x) - remove a primeira ocorrencia do item x, se x não for encontrado teremos Valueerror
- lista[pos] - retorna elemento da lista na posição pos
len(lista) - retorna o comprimento da lista
- lista.count(elemento) - retorna quantas vezes elemento ocorre na lista
- lista.sort() - ordena o conteudo da lista de mesmo tipo. 

def removeDuplas(elem):
        indice = 0
        while indice < len(elem):
                if elem.count(elem[indice]) == 1:
                        indice += 1
                else:
                        elem.remove(elem[indice])
        return None

- Fatiamento de listas : Podemos retornar uma nova lista composta de referencias para os elementos existentes, iniciando-se por elemento da posInicio e finalizando por elemento na posFinal - 1. lista[1, 4]  - teremos elementos 1, 2 e 3. Pode ainda ter um terceiro parametro de contagem, marcando de quantos em quantos elementos pegaremos

## Lista de Listas

Mercado = [["pera", 100, 4. 9]]
mercado[0][2] -> é o 4.9

- Podemos usar remove para remoção de uma sublista de lista. mercado.remove(["pera", 100, 4. 9])
- Podemos inserir com insert. mercado.insert(1, ["kiwi", 20, 10])

- No sentido de exercitar a elaboração de subprogramas recursivos apresentadmos as tres operacoes primitivas do paradigma de programação funcional da linguagem LISP(list processing)
        - car(dados) - operação seletora que retorna primeiro elemento de lista
        - cdr(dados) - operação seletora qie retorna o resto da lista de dados, isso é, retorna todos elementos menos o primeiro
        - cons(item, dados) : operação construtora que retorna lista que contém o item como primeiro elemento seguido pela lista de dados

        def car(dados):
                return dados[0]
        def cdr(dados):
                return dados[1: len(dados)]
        def cons(item, dados):
                return [item] + dados

        isInstance(item, list)

## Arquivos de Texto

- Programas interativos leem os dados de entrada do teclado e apresentam dados na saída da tela
- Arquivos são utilizados para armazenar os dados de entrada e os de saída
- Arquivo texto é sequencia de caracteres organizada em linha. Podem ser criados, visualizados e alterados por editores e processadores
- \n indica fim de linha e \0 é o fim de arquivo

- Antes de ser utilizado um arquivo de texto precisa ser associado a um nome no diretório de arquivos a ser aberto via OPEN:
        variavel = open(caminho do arquivo)
        variavel = open(caminho do arquivo, modo)
- os modos de operação são r, de apenas leitura e w de apenas escrito. o modo a escrita apenas no final do arquivo, o r+ é para leitura e escrita

dados = open("teste.txt", "r")
A cabeça de leitura aponta para primeiro caracter da primeira linha, se ele não existir teremos um erro. Se quisermos apenas concatenar no final do texto devemos utilizar "a". Se utilzarmos o "w" escreveremos no inicio.

-dados.close() - >fecha leitura ou abertura
- linha = dados.readline() - >le linha completa com a \n incluso, para imprimir basta usar print(linha, end="")
- Cada realine() vai movendo a cabeça de leitura ou escrita
- para ler todas as linhas de uma vez devemos readlines() -> só funciona para pequenas arquivos. 


``
def le_texto():
    with  open("./teste.txt", "r") as file:
        for line in file:
            print(line.strip())

le_texto()


ou 


dados = open("exemplo.txt", "w")
linha = dados.readline()

while linha != "":
        print(linha, end="")
        linha = dados.readline()
dados.close()


ou


for linha in dados:
        print(linha, end="")
dados.close
``

- Para método de Escrita, usamos o write(), escreve no ponto de onde está a cabeça de escrita


``
dados = open(teste, "w")
dados.write("teste") - escreve
dados.close
``

``
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
``

Para copiar

orig = open("nomeOrigem", "r")
dest = open("nomeDest", "w")

for linha in orig:
        dest.write(linha)
orig.close()
dest.close()


- Para anexar nova linha ao final do arquivo devemos usar o modo "a"

arquivo = open(nome, "a")
novaLinha = input(diga nova linha)
arquivo.write(novalinha + '\n')
arquivo.close()

- Tratamento de Exceções são importantes para evitarmos erros

