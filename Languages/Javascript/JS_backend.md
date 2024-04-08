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

.lenght - retorna tamanho array
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

## Procurando em Lista

lista.includes(nome) -> true ou false
indice = lista.indexOf(nome)

## Desestruturar

const [alunos, medias] = lista
Desestruturo o array em dois.

## Percorrer Lista

for(let i = 0; i < tamanholista; i++)
{
        ação
}

reverso:

for (let i = numeros.length - 1; i >= 0; i -= 2) {
  console.log(numeros[i]);
}

- Podemos percorrer com for of e temos acesso ao numero do elemento

for(const itens of lista)

let iterable = new Map([["a", 1], ["b", 2], ["c", 3]]);

for (let entry of iterable) {
  console.log(entry);
}
// [a, 1]
// [b, 2]
// [c, 3]

for (let [key, value] of iterable) {
  console.log(value);
}
// 1
// 2
// 3

for(let [key, value] of nums.entries())

O loop for...in irá iterar sobre todas as propriedades enumeráveis de um objeto. Ele pega as chaves e percorre elas.

A sintaxe do for...of é específica para coleções, ao invés de todos os objetos. Ela irá iterar desta maneira sobre os elementos de qualquer coleção que tiver uma propriedade.

## For each

- Para cada item faça...
- Recebe função callback

notas.forEach(function(nota){
        somaNotas += nota;
})

notas.forEach((nota) =>{
        somaNotas += nota;
})

## MAP

- método que podemos usar em array
- método retorna algo porque ele cria novo array modificado

const novasNotas = notas.map((nota) =>
{
        return nota + 1;
})

## Filter

- retorna array filtrado
- É método callback
- Filtra elemento baseado em True e False, ve se questão é true ou falso e devolve apenas os verdadeiros em novo array

const tamanhoNome = aluno.filter((aluno, indice) =>{
        return aluno.length < 4
})

## Reduce

- Usado para somar valores
- recebe dois parametros, uma função callback e um valorInicial para ser somado


const somaNotas = lista.reduce((acumulador, nota) =>{
        return acumulador + nota;
}, valorInicial)

## Clonando Arrays

- Quando atribuimos uma lista a uma variavel nós não temos o valor do array, temos uma referencia ao array. Assim se mudamos algo alteramos ambos os arrays.

- Podemos usar spread operator. Ele pega o array e espalha em novo array.

const notas = []
const novaListaNotas = [... notas, 10]

## Remover duplicadas

- Set é conjunto de dados que armazena valores unicos.
- é array like mas não tem métodos de array
- Posso retransformar em array.

const nomes = []
const nomesAtualizados = new Set(nomes);
const listaNomes = [... nomesAtualizados]

