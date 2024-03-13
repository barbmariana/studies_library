# Estrutura de dados UFF

## O conceito de Algoritmo

Processo sistemático de resolver problemas. 
Entrada -> Algoritmo -> Saída

## Linguagem Utilizada

Linguagem tipo pascal. Linguagem identada em blocos.

Variáveis:
i, j

Vetores:
x[i] 
x[5] - > quinto elemento

Matrizes:
x[i, j]

Ponteiro:
 ↑
ex: pt ↑.info -> o campo info de registro alocado no endereço contido em pt

Procedimentos:
Um procedimento é chamado através da ref a seu nome.
ex:
A

proc A

Funções:
é chamada através da ref a seu nome. Ela retorna valor

função A(B)
ex:
A(B)

Comentários:
Sentença iniciada por %

Atribuição:
:=

Condicionais:
Se A então B

ex:
se x>y então
        x:=[y]
senão
        x:= a + i

Iteração:
Enquanto A faça B ( while)
ou
para A faça B ( for)
repetir ( do while)
até que

ex:
enquanto i != 0 faça
        x := a[i, j]
        i := i - 1

para i = 1, 2 ... n faça
        j := 3a - i

repetir
listar x[i, j]
        i := i - a
        j := j + 1
até que i < j

Declaração Parada:
pare

exemplo:
se i < 0 então pare

Piso de x [x] representa o maior inteiro <= x

Teto de x [x] representa o menor inteiro >=x

ex:
piso de [3,2] é 3
teto de [3,2] é 4

Propriedade: piso n/2 +  teto n/2 = n


Inversão Sequências:

para i = 1 até piso de n/2 faça
        temp := s[i]
        s[i] := s[n - i  + 1]
        s[n - i + 1] := temp


## Recursividade
Procedimentos e funções que chamam a si mesmo. Procedimentos são rotinas e funções são procedimentos que retornam algo. Todo procedimento recursivo ou não deve possuir pelo menos uma chamada não recursiva.



