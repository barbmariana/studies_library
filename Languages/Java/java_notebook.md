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

## Primary types

Integers: Int (32bits), Long(64bits), Short(16bits), Byte(8bits).
Floats: Float(32 bits), Double(64bits)
Caracter Unicode: char (16 bits)
True or false value: boolean (1bit)

## Non primary types
String : string of characters - always with caps S.
String str = "teste";
or
String str1 = new String("teste"); --> each time you call this a new object it's going to be created
Array: Sequence of any type, but always with a single type.

int arr[]; --> declare the array
arr = new int[2]; --> declare the size array
If I print the array, it will print the local of the memory, thats why I can print letter by letter.


## Basic operations

Data entry - entry devices - reading
Processamento de Dados - Dentro do processador, onde calculos são realizados.
Saída de Dados - Saída por dispositivos de Saída - Escrita

## Data exit

Its called writing, the program is writing data. 

- System.out.print("Hello World");
- System.out.println("Bom dia"); --> Tem quebra de linha no final

We can call our own variable inside the (). 

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

## Processamento de Dados

Comando de atribuição. Variáveis recebem expressões
Primeiro a expressão é calculada e depois a expressão recebe o valor. 

int x, y;
x = 5;
y = x * 2;

y vale 10 agora. 

## Casting
int a, b;
double res;

a = 5;
b = 2;
res = a / b --> compilador decide que inteiros por inteiros da um inteiro
Para eu forçar o tipo é só eu fazer um casting, que é colocar na frente (double)
Posso forçar tipos, converter para outro desde que eu não me importe em perder partes

## Data entry

Em java precisamos criar um objeto do tipo Scanner

Scanner sc = new Scanner(System.in) --> preciso import java.util.Scanner

Ex:
import java.util.Scanner;

Scanner sc = new Scanner(System.in) --> associando o Scanner ao meu teclado
String x;
x = sc.next();
sc.close();

Para digitar num inteiro devo usar sc.nextInt()
Para digitar um float devo usar sc.nextDouble();

Lembrar que preciso mudar o locale para o US para vermos o ponto e não a virgula. 
Se eu to no brasil eu preciso botar o 4,5 e não 4.5

Para ler caracter devemos usar a variavel do tipo char, e depois botar charAt(0)
ex:
char c;
x = sc.next().charAt(0);

Para ler varios dados na mesma linha chamamos cada um com seu respectivo next
Eles devem ser inseridos separados por um espaço. 


x = sc.next();
y = sc.nextInt()
z = sc.nextDouble()


Lembrando que se queremos ler um texto de entrada todo, devemos usar o nextLine

Quando usamos o next apenas ele le apenas a primeira palavra, para ler até a quebra de linha usamos o nextLine
Quando usamos um comando de leitura diferente do nextLine e damos uma quebra de linha, essa quebra fica pendente na entrada padrão
Se fizermos então um nextLine logo abaixo a quebra de linha vai consumir ele e vai pular para o próximo comando.
A solução é fazermos um nextLine() extra, sozinho sem entrar em nenhuma variável


## Funções Matemáticas Java

A = Math.sqrt(x); --> A recebe raiz quadrada de x
A = Math.pow(x, y) --> x elevado a y
A = Math.abs(x) --> Variavel A recebe o valor absoluto de x

## Operadores Comparação e Lógicos

< > <= >= , !=, &&, ||, !

E - && -> Toda a expressão deve ser verdadeira
Ou - || -> Apenas uma das expressões deve ser verdadeira

## Condição If Else

Estrutura condicional, de controle, que permite definir um certo bloco de comando
Tudo que tiver dentro de estrutura deve estar identado

``
        int idade;
        boolean carteira;

        Scanner sc = new Scanner(System.in);
        System.out.print("Qual a sua idade: ");
        idade = sc.nextInt();
        System.out.print("Tem carteira: ");
        carteira = sc.nextBoolean();

        if(idade < 18){
            System.out.println("Menor de idade, não pode dirigir");
        } else if (idade >= 18 && !carteira) {
            System.out.println("Maior de idade, mas não tem carteira");
        }
        else{
            System.out.println("Maior de idade, e tem carteira, pode dirigir.");
        }

        sc.close();

``
## Switch Case
Igual em outras linguagens

Switch(x)
    case 1: 
        dia = "Domingo";
        break;
...
    default:
        dia = "valor invalido"
        break;

## Operador Ternário

(condicao) ? valor_se_verdadeiro : valor_se_falso

## Escopo
Região onde variável é valida, onde pode ser referenciada.
variável não pode ser usada se não for inicializada
Se eu declaro variáveis dentro de blocos if, switch eu preciso declarar ela fora. O compilador entende q se vc inicializar
uma variável apenas em determinada condição, ela vai precisar ser inicializada antes do bloco ou coloque um outro valor para else

## While 
Estrutura de controle que repete bloco de comando enquanto condição for verdadeira. 
Usamos quando não sabemos previamente a quantidade de repetições a ser realizada, e também quando queremos botar o incremento apenas
dentro de blocos

while (condicao)
{
    comando 1
    comando 2
}

ex:
Scanner sc = new Scanner(System.in);

        int x;
        int soma = 0;
        x = sc.nextInt();

        while(x != 0)
        {
            soma += x;
            x = sc.nextInt();

        }
        System.out.println(soma);
        sc.close();
    


## Estrutura For
Estrutura de controle que repete bloco de comandos para intervalo de valores
Usamos quando sabemos previamente a quantidade ou intervalo de valores

for(inicio; condicao; incremento)
{
    comando;
}

``
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int soma = 0;
for(int i = 0; i < n ; i++)
{
int num = sc.nextInt();
soma += num;
}
System.out.println(soma);
``
## Do While

Bloco de comando é executado pelo menos uma vez. O do é feito antes, depois testamos
o while que decide se vai voltar ou sair do bloco. 

## Padrões Java
Tudo começa com minusculo e usa CAmel Case, menos classes onde usamos maiusculo e
Pascal Case

## Operador Bitwise
Operador Bit a Bit. Pega cada bit e faz a comparação. 
& - E bit a bit
| - Ou bit a bit
^ - Xor bit a bit

## Funções para String
toLowerCase, toUpperCase, trim(remove espaços)  -- Não mudam a original
substring(inicio), substring(inicio, fim), replace(char, char)
replace(string string), indexOf, lastIndexOf, Split(separar)


- Trim:
Não muda a original
``
String a;
a = "   aMSajfo asfSFF";
System.out.println(a.trim());  --> Vai tirar os espaços em branco do começo
``

- Substring
Posso fazer com a posicao inicial, ou com a inicial e final.
Começa a pegar a posição inicial até antes da final. 

``
String a;
a = "aMSajfo asfSFF";
System.out.println(a.substring(2));
``

- Replace
Troca o primeiro pelo segundo em todas suas ocorrências
``
  String a;
  a = "aMSajfo asfSFF";
  System.out.println(a.replace('a', 'x'));
``
- IndexOf
Achar a primeira ocorrência de determinada string
- LastIndexOf 
Achar a ultima ocorrencia de determinada string
- Split
Recebe separador e gera vetor com as partes da string separadas


## Comentários

Comentário de bloco /**/
Comentário de linha //

## Funções

Representam processamento que possui significado. Modularizacao, Delegação, Reaproveitamento
Recebe dados de entrada e saída
Em Orientação a objetos as funções são chamadas de métodos
Colocamos a função dentro da classe.
Public é para que possa ser acessado em outro escopo. Static é para representar que será o mesmo objeto se chamado em dif esclass

    public static  int max(int a, int b, int c){
        if(a > b && a > c)
        {
            System.out.println("O Maior num é " + a);
            return a;
        } else if(b > a && b > c)
        {
            System.out.println("O Maior num é " + b);
            return b;
        } else
        {
            System.out.println("O Maior num é " + c);
            return c;
        }
}
## POO

Classe é tipo estruturado que pode conter membros, sendo eles Atributos e Métodos
Atributos tem dados e campos. Métodos são funções e operações
Pode prove muitos recursos como Construtores, Sobrecarga, Encapsulamente, Herança, Polimorfismo

Ex:

Entidades: Produtos, Cliente, Triangulo
Serviços: ProdutoService, ClienteService, EmailService, StorageService
Controladores: Calculadora, Compactador
Outros: Views, Repositórios, Gerenciadores

ex Classe para representar triangulo:
Entidade que representa o triangulo. Variaveis public para serem
acessadas por outros atributos


public class entities.Triangle{
    public double a;
    public double b;
    public double c;
}

entities.Triangle x, y;  --> Criando objeto
Instanciando Objeto:

x = new Tryangle();
y = new Tryangle();

        Scanner sc = new Scanner(System.in);

        Triangle x, y;
        x = new Triangle();
        y = new Triangle();
        x.a = sc.nextDouble();
        x.b = sc.nextDouble();
        x.c = sc.nextDouble();
        y.a = sc.nextDouble();
        y.b = sc.nextDouble();
        y.c = sc.nextDouble();


Quando fazemos a declaração da variável do tipo de classes elas são
criadas em area da memória chamada STACK. Onde são criadas as variáveis static.
Quando instancio eu to criando numa area da memória chamada HEAP. 
A variável X que criamos e está na stack tem o endereço que aponta para o valor que está no heap, instanciadas. 

## Referenciar próprio atributo e Métodos
Usar a palavra This .
``
public double totalValueInStock(){
return price * qtd;
}
public void addProducts(int qtd){
this.qtd = this.qtd + qtd;
}
public void removeProducts(int qtd){
this.qtd = this.qtd - qtd;
}
// No main -->
Locale.setDefault(Locale.US);
Scanner sc = new Scanner(System.in);
Produto produto1;
produto1 = new Produto();
System.out.println("Entre com o produto: ");
System.out.println("Name: ");
produto1.name = sc.nextLine();
System.out.println("Price: ");
produto1.price = sc.nextDouble();
System.out.println("Quantidade : ");
produto1.qtd = sc.nextInt();
System.out.println(produto1.name + ", R$" + produto1.price + ", " + produto1.qtd + " em estoque");
sc.close();
``

## Classe object
Toda classe em java é subclasse ta classe object.
Object possui alguns métodos, getclass que retorna o tipo. Equals que compara se objeto é igual a outro.
hashCode retorna código hash do objeto. toString que converte o obj para string

## To string
Um método que já vem pronto mas podemos sobrepor criando um método em nossa classe
Criamos um método toString na classe que vai mudar a saída

Chamada no Main:
``
//produto1.toString();
System.out.println(produto1);
``

Sobrepondo o método:
``
public String toString(){
return (name + " , " + price);
}
``
