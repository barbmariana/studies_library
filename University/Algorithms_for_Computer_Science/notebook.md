# Algorithms for Computer Science

## Conjuntos

Estrutura Comum em:
- Equipe de futebol - Grupo de jogadores
- Rebanho de ovelhas - Reunião de ovelhas
- Biblioteca - coleção de livros

São coleções de objetos

Noção intuitiva:
Um conjunto é uma coleção de objetos chamados elementos

Usamos letras maiuscúlas para nomear conjuntos. A e B por exemplo. Usamos letras minúsculas para descrever elementos do conjunto

Exemplo:

Elementos do meu conjunto B podem ser denominados por m monitos, t teclado, c adeira, v você
O símbolo { } indica início e fim de descrição de conjunto

B = {m, t, c, v}
t ∈ B

- Relação de pertinência : O elemento t está no conjunto
 B - >  t pertence ao conjunto X. Lembrar que conjuntos não podem pertencer a outro, apenas conter.

 Pertinência : x pertence a um conjunto X se x é um elemento de X -> x ∈ X

N -> conjunto de números naturais (inteiros não negativos)

10598 ∈ N

- Coleções devem ser bem definidas. Um conjunto é uma coleção BEM DEFINIDA de objetos chamados elementos. Ou seja, sempre podemos decidir quando o objeto está ou não no conjunto

Representação explícita:
- Enumeração dos elementos do conjunto
- B = {m, t, c, v} N = {1, 2, 3...}

Representação implícita:
- Indicação da propriedade que caracteriza os elementos
- C = conjunto das pessoas que têm mais de 1, 75 metros de altura -> C está constituído por elementos(pessoas) x tal que a altura de x é maior que 1, 75 metros -> 

C = {x | altura de x > 1,75 metros} 

Propriedade que caracteriza os elementos de C - > P(x) : altura de x é maior que 1,75 metros
C = {x | P(x)}

O símbolo | significa tal que. Depois segue a verificação

### Exemplo :

D = conjunto de números naturais maiores ou iguais a 5

Representação explícita:

D = {5, 6, 7, ...}

Representação implícita:

D = {x | x ∈ N e x >= 5}
P(x) = x ∈  N e x >= 5

## Notação de conjuntos conhecidos

N = conjunto dos números naturais
N = {1, 2, 3, 4, 5, ...}
Z = conjunto dos números inteiros
Z = {..., -2, -1, 0, 1, 2, ...}
Q = conjunto dos números racionais
Q = {x | x = p/q, p, q ∈ Z, q != 0}
R = conjunto dos números reais
Conjunto vazio é conjunto sem elementos, representado por bola cortada. Ele é um conjunto bem definido.

o = {x | x ∈  N, x > 5 e x < 0}
o = {x | x ∈ Z, 2x -1 = 0}

## Relação de conjuntos

- Definição de igualdade. Conjuntos de A e B são iguais quando têm os mesmos elementos. Notação A = B

A = 1, 3, a
B = 3, a, 1
C = 1, 3, 1, a
D = 2, 3, a

A = B = C
A != D

Mesmo que C tenha elemento a mais ele também está em A. Então são iguais. Para testar igualdade devemos ver se todos os elementos contém no outro conjunto, e se todos desse outro contém no primeiro conjunto.

- Definição de inclusão:
Um conjunto A está contido em um conjunto B se todo elemento de A é elemento de B

A contém B . A está contido em conjunto B se todo elemento de A é elemento de B. A ⊂= B

N = { 1, 2, 3, 4,...}
P = {2, 4, 6, 8...}
S = {0, 1}
P está contido em N
S não está contido em N

A ⊂= B e B ⊂= A ou seja A = B
A é subconjunto em B
B contém o A -> B ⊃= A

## Definição de inclusão estrita:

A ⊂ B e A está contido estritamente em B. Ou seja, B não está contido em A. Então tiramos o igual de baixo

PAra todo conjunto : 0 ⊂= A
Para todo conjunto A != 0 : 0 ⊂ A

## Conjunto de partes de conjunto

- Conjunto de A:
Conjunto das partes de A é P(A), é o conjunto formado por todos os subconjuntos de A

Seja A = {1, 2, 3}
então
P(A) = {vazio, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}

O conjunto vazio está contido em todos os conjuntos.


![alt text](image.png)


Exercícios:

 { x ∈ | |x| ≤ 4 } onde |a| = a se a ≥ 0 ou |a| = -a se a < 0
 (Observação: |x| ≤ 4 é equivalente a -4 ≤ x ≤ 4 )

(iii) ∅ ∈/ P(A), onde A = {1, 2}
Resposta: FALSA, pois P(A) = {∅, {1}, {2}, {1, 2}} e ∅ é um elemento do conjunto P(A), logo ∅ ∈ P(A).

(iv) {1} ∈ {x ∈ R|x^2 = 1}
Resposta: FALSA, pois {1} não é um elemento do conjunto {x ∈
R|x
2 = 1}, já que este conjunto é formado apenas pelos elementos 1 e −1, temos 1 ∈ {x ∈ R|x^2 = 1} e {1} ⊆ {x ∈ R|x
2 = 1}.

(ii) {π} ⊂ {1, {π}, a}
Resposta: FALSA. De fato, π não é um elemento de {1, {π}, a}. Portanto, a definição de inclusão estrita não é verificada.
(iii) {{π}} ⊂ {1, {π}, a}
Resposta: VERDADEIRA

(iv) ∅´não está contido em  {3, 1, −7}
Resposta: FALSA, pois ∅ ⊆ C, para todo conjunto C

Atentar que quando for relação de pertencimento, estamos fazendo uma comparação de elemento que deve pertencer a algum conjunto. Já o contém é uma relação onde todos os elementos estão contidos em um conjunto. Então comparamos tudo dentro do {} com o outro conjunto. REpare no exercício ii e iii

## Diagramas de Venn

D = { x | x pertence a N e x >= 5} = {5, 6, 7,...}
A = { x | x pertence a N e x^2 = 36} = {6}

Conjunto Universo : Aquele que contém todos os conjuntos de determinado contexto. Denotado pelo U. Todo conjunto está contido no conjunto universo.

A = {x pertence U | P(x)}
Elementos de x pertencem a U tal que x verifica propriedades de partes de x

- O diagrama de Venn é a representação visual de conjuntos, suas operações e relações

![alt text](image-1.png)

A está contido estritamente em um conjunto universal. 

![alt text](image-2.png)


## Operações 

- União :
        Sejam A e B subconjuntos de U, a união de A e B é A U B é o conjunto formado por todos os elementos que pertencem a A ou que pertecem a B
        A = {1, 2, 3, 4, 5, 6}
        B = {5, 6, 7, 8, 9}
        A U B = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        A está contido na união e B também
        Caso o conjunto esteja contido todo no conjunto maior, a união é apenas o conjunto maior
        Propriedade = A está contido em B então A união B é igual a B
        A U B = B -> A está contido em B
        A está contido em B si e somente si A união B = B
        A contido em Universo.A união A = A. A união vazio = A
- Interseção:
        Sejam A e B subconjuntos de U. 
        Interceção de A e B que denotamos A U(invertido) B é o conjunto formado por todos os elementos que pertencem a A e ao conjunto B. A interse B = { x pertence U | x pertence A e x pertence B}
        A = {1, 2, 3, 4, 5, 6}
        B = {5, 6, 7, 8, 9}
        A intersec B = {5, 6}
        Propriedade = A intersec B contido em A e A intersec B contido em B
        Z intersec W = W se W contido em Z. A esta contido em B se e somente se A intersec B = A
        Se A está contido em U temos A intersec A = A e A intersec vazio igual a vazio
- Diferença:
        Sejam A e B subconjuntos de Universo
        A diferença entre A e B ( A - B) é o conjunto formado por todos os elementos que estão em A e não está em B
        A - B = X percente a U | x pertence a A e não pertence a B
        A = {1, 2, 3, 4, 5, 6}
        B = {5, 6, 7, 8, 9}
        A - B = {1, 2, 3, 4}
        Propriedade = A - B contido A e B - A contido C
        z = altura de x >= 1,75
        w = altura de x >= 1,90
        Z - W = Z - W contido em Z -> x >=1,75 e x < 1,90
        W - Z = vazio     A está contido em B se e somente se A - B = vazio
        A - A = vazio
        A - vazio = A
- Complemento:
        Sejam o conjunto universo U e o conjunto A contido em U:
        O complemento de A que denotamos A(com traço em cima) é o conjunto formado por todos os elementos de U que não estão em A. A(traço) = U - A
        U = N
        A = { x pertence N | x <= 50}
        A(traço) = N - A = {x pertence N | x > 50}
        U = Z
        A = { x pertence Z | x > 2}
        A(traço) = {x <=2 } -> 2, 1, 0, -1...

![alt text](image-3.png)
- Comutatividade:
A união B = B união A
A interseção B =  B interseção A

- Associatividade:
(A união B) uniao C = A união (B união C) = A U B U C
(a inter B) inter C = A inter B inter C

- Distributividade:
A união (B intersec C) = (A uniao B) intersec ( A uniao C)

## Leis de Morgan:
Complemento de A U B = U - (A U B)
traço traço (A união B) = traço A intersec traço B .  Colocamos o traço e união vira intersec
A uniao B ( traco) = A(traço) intersec B(traço)

![alt text](image-4.png)

(a intersec b) traço = A(traço) uniao B(traço)

![alt text](image-5.png)

## Prova formal de identidade 5

![alt text](image-6.png)

## Resumo

![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)
![alt text](image-10.png)


## Números de elementos

n(A) : número de elementos de conjunto de A ( cardinalidade de A)

A = { x pertence Z | |x| <=3} = -3 <= x <= 3
n ( A) = 7

- Podemos ir enumerando os elementos de conjunto mas nem sempre poderemos contar todos os elementos
- Conjunto finito  - Possível de contar números de seus elementos
- Conjunto infinito - Não é possível contar o número de seus elementos

- Apesar de ser finito, alguns conjuntos não são possíveis de serem contados

- Princípio Aditivo:
Se A e B são disjuntos, A intersec B = vazio
então n(A U B) = n(A) + n(B)

- Princípio da inclusão ou exclusão:
Dados conjuntos A e B, calcular n(A U B), mas eles tem intersec diferente de vazio
N(A U B) = n(A - B) + n(A intersec b) + n(B - A)
N(A) = n(A - B) + n(A intersec B)

ou
N(A U B) = n(A) + n(B) - n(A intersec B)

- Princípio inclusão e exclusão para três conjuntos

n(A U B U C)
n(A) + n(B) + n(C) - intersec + n(A intersec B intersec C)

na hora de eliminar interseções eu to eliminando a mais, por isso somo de novo

## Princípio da indução matemática
Técnica para provar resultados matemáticos. Provar resultados que envolvem os números naturais

PIM -> Princípio da indução matemática

Idéia intuitiva -> Se algo vale para o caso base ele vai valer para todos os próximos casos

seja P(n) uma afirmação, para cada n pertencente a N
P(1) verdadeira e
P(k) verdadeira -> P(k + 1)
P(n) é verdadeira para todo n pertencente a Naturais

1 - Base da indução:
Mostrar que P(n) verdadeira para n = 1

2 - Hipótese de indução:
Assumir que P(k) verdadeira para k >= 1

3 - Passo indutivo:
Mostrar que P(k + 1) verdadeira assumindo 2

Exemplo:

Soma de números de sequência - n(n + 1) / 2

prova que P(n) = n(n+1)/2

1 - Base da indução:
P(1) = 1(1+1) / 2 = 1 VERDADEIRA

2 - Hipótese de indução (HI) - Assuma que P(k) é verdadeira, k >=1
P(k) = k(k+1) / 2

3 - Passo indutivo - se P(k) é verdadeiro P(k + 1) é verdadeiro

soma de K = k(k + 1) / 2
soma de K + 1 = k(k + 1)/ 2 + k + 1
(k^2 + k)/2 + (k + 1) = 
(k^2 + k + 2k + 2)/ 2
k^2 + 3k + 2 -> 
(k+1)(k+2) / 2 - > n(n+1) / 2
é VERDADEIRO

Então pelo pim P(n) = n(n + 1) / 2 -> verdadeiro

![alt text](image-11.png)


## Indução Forte



 

