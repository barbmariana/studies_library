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


