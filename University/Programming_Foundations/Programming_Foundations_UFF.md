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

# Estrutura seleção com dois ramos

if <condicao>:
        ...
else:
        ...

# Estrutura de seleção aninhadas

if <condicao> :
        ...
elif <condicao>:
        ...
else:
        ...

# Split
Divide a string, considerando o espaço em branco como separador, em uma lista de substrings

valores = input("Entre com dois números:").split()
x = int(valores[0])
y = int(valores[1])

# None

É o tipo nenhum. Ele denota falta de valor.

# Estrutura de repetição indefinida (WHILE)
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

# Estrutura de repetição definida (FOR)
É utilizada quando sabemos os números de repetições

for <var> in <list>:
        <suite>
A cada repetição, var assume o valor do item

for item in {3, 4, 5, 6}:
        print(item, end=" ")
print()  //aqui ele pula a última linha

# Range
Para criar uma lista com uma progressão aritmética de elementos, podemos utilizar range

range(valor limite) - Cria uma lista com progressão dos itens de razão 1 iniciada no zero até o limite, lembrando que ele segue até o valor que antecede o limite. 

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





