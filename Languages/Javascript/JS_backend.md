# Javascript for Backend

É uma linguagem interpretada e o navegador interpreta o seu código. Ela é multiparadigma, e pode ser utilizada OO, funcional ou procedural.

## Node JS

O navegador é o interpretador original do JS. O node é um interpretador fora do navegador. 

## Variáveis
Utilizamos let, var e const para definir variáveis. O var é global. Const não pode ser alterado. 

let estudante = 'Caroline';

O que vai mudar é o escopo da variável. O var é uma variável global enquanto o let define variáveis de bloco e função. 

## Number

Javascript aceita como valores numéricos valores inteiros e flutuantes. Devemos colocar o numero fora de strings, se não em contas ele vai concatenar.

Para converter string para número podemos usar Number.parseInt(variavel) ou parseFloat().

NaN -> not a Number. 

Podemos testar com Number.isNaN(numero)
Number(variavel) - converte para num. 

## String

Qualquer caracter dentro de aspas duplas ou simples. 

Para concatenar basta usar o sinal + entre strings. 

Template String
` Essa é uma string ${stringTemplate}`

método de upper e lower
variavel.toUpperCase();
variavel.toLowerCase();
String() -> converte para string
.includes() -> retorna true ou false dependendendo se string possui valor passado entre parenteses

## Typeof

Para descobrirmos o tipo do dado podemos usar o operador typeof 

typeof variavel

## Boolean

Dois valores possíveis :
True e False

## Null of undefined

Undefined ocorre quando o valor é não definido. Null é quando o valor está vazio.

## Operadores 

<=
>=
== Testa se é igual
=== Testa se é identico, valor e tipo
!= diferente
!== não identico
|| Ou
&& End
! Not
? : -> ternário


## Funções

function nomeFuncao(parametro)
{
        return...
}
const nomeFuncao = (parametro) => {

}

const nomeFuncao = function(parametro) {

}

## Arrays
São listas de dados guardadas em uma mesma variável. São dados do mesmo tipo(em estrutura de dados, mas não em js)


const notas = [10, 6.5, 8, 7.5]
Cada item é acessado por seu index. Iniciando do zero.

.lenght() - retorna tamanho array
.push() - adiciona item no final da lista
podemos adicionar também pelo indice
.pop() - removemos um item do final da lista
Podemos dar push e pop em variáveis consts, elas só não podem ser reatribuidas

.slice():
Criar novas listas a partir de uma.
Parametros - inicio, fim(opcional)
variavel = .slice(inicio, fim) - o fim é opcional. O paramatro de fim determina que o slice vai até um item antes desse fim

.splice():
Forma de manipular lista. Deletamos os elementos da própria lista. Podemos adicionar elementos na lista também. 
Parametros  - inicio, numero de elementos, elemento incluido(opcional)
variavel.splice(1, 2, "nome") - > vai retirar o item 1 e 2 e adicionar o nome. 

.concat():
Concateno dois arrays e insiro em um novo array. 
const novaVariavel = nomeVariavel.concat(nomeVariavel2);


Array duas dimensões:
const alunos
const medias
const lista = [alunos, medias];
Para acessar basta usar variavel[][]