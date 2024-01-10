# Java Notebook

Java is a Object Oriented Language that was created to help programming different things as computer programs, eletronics and cars and houses utensils programs.

## How to Create a Java program

The program runs inside the principal class called MAIN.
``
public class application.Main {
public static void main(String[] args) {
String    name;
name = "Obrigada";
System.out.println("Muito "+ name);
}
}
``

To compile your program you can use :
javac nameofyourarchive.java

To run :
java nameofyourexecutable.class


## Operators

+, -, *, / , % 
Order: 
1 - * / %
2 - + -


## Variables

I return a value in the Ram memory to save a data type. We have to choose names that starts with letters or _. 
If i want to create constants I can use the word FINAL as:

final int i = 5;

``
char name = "Mariana";
int age = 26;
double height = 1.63;
double weight = 62.5;
double imc = weight / height*height;
``

## Tipos Primitivos

Inteiros: Int (32bits), Long(64bits), Short(16bits), Byte(8bits).
Floats: Float(32 bits), Double(64bits)
Caractere Unicode: char (16 bits)
Valor Verdade : boolean (1bit)

## Tipos não primitivos
String : Cadeia de Caracteres - Sempre com S maiusculo
String str = "teste";
ou
String str1 = new String("teste"); --> Cada vez que você chama ele criará um novo objeto
Array: Sequencia de qualquer coisa, numeros, caracteres. Mas sempre de forma homogênea, todos do mesmo tipo. 
int arr[]; --> declara o array
arr = new int[2]; --> declara o tamanho do array
Se eu coloco para imprimir o array, ele imprimirá o local da memória, posso imprimir letra por letra. 

## Operações Básicas de Programa

Entrada de Dados - Entrada por dispositivos de entrada - leitura
Processamento de Dados - Dentro do processador, onde calculos são realizados.
Saída de Dados - Saída por dispositivos de Saída - Escrita

## Saída de Dados

Chamada de Escrita, programa está escrevendo Dados. 

- System.out.print("Hello World");
- System.out.println("Bom dia"); --> Tem quebra de linha no final

Posso chamar a própria variável dentro dos parenteses. 

Para escrever conteúdo de variável com ponto flutuante podemos só chamar a variável, ou podemos usar os placeholders. 
System.out.printf("%.2f%", x). Assim eu consigo definir quantas casas decimais eu quero, mas ele coloca virgula e não ponto. 

printf --> Deixa a gente formatar a saída, pega o formato do padrão do computador que estamos usando.

Locale.setDefault(Locale.US); --> Para mudar o local para US e a virgula virar ponto. Devo importar com
import java.util.Locale;

Podemos concatenar as partes com operador +.
Podemos também usar o printf e colocar os placeholders marcadores. 
"resultado é %.2f metros" - flutuante

%f --> flutuante
%d --> inteiro
%s --> texto
%n --> quebra de linha

Quando o dado for de precisão dupla, double, colocamos seu valor com o ponto mesmo que não tenha
tipo x = 6.0. Caso seja float podemos usar o b = 6f.
