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

## Metodos de string

- Substring() - index de inicio mais um index antes do fim. substring(0, 3) -> pega tres itens

## Objetos

``
const pessoa = {
        nome: 'Mariana',
        idade: 27
}
``

- Podemos acessar com o operador '.' -> pessoa.nome = 'Mariana' ou com o '[infoEStudante]'. Atraves do operador ponto podemos também alterar um atributo do objeto.

- delete pessoa.nome -> deleta propriedade nome

- Funções em objetos representam seus comportamentos

### Iterando sobre objetos

- For in - for(let chave in estudante){
        console.log(chave)
} - Percorremos cada chave do objeto, para vermos os valores basta usarmos estudante[chave]

- For of - > Usamos mais para arrays, iterar sobre itens de array

- Object.keys(estudante) -> Teremos aqui a lista de chaves

- Object.values(estudante) -> retorna array dos valores

- Object.entries(estudante) -> retorna arrays de chave e valor - Arrays de arrays com chave e valor 
for of[ [ 'nome', 'Mariana' ], [ 'idade', 27 ] ]

### JSON

JavaScript Object Notation
- Não é tipo de dado JS
- Não precisa ser declarado

{
        "nome":"Mariana",
        "idade":32
}


- Para salvar em variavel:
const estudante = require('./estudante.json')
consts chaves = Object.keys(estudante)

- JSON.Strongify - Transforma json em string
- JSON.parse - Transforma a string em objeto

## Metodo Find X Filter

- Metodo find encontra o primeiro objeto que tem determinada propriedade
- Metodo filter retorna um array de todos elementos que atendem determinada condição

## Metodo Sort

- Tem dois parametros (a, b)

function ordena(lista, propriedade)
{
        return lista.sort((a, b) =>
        {
                if(a[propriedade] < b[propriedade] return -1)
                return 1;
        })
}

## Membros estáticos
Membros são atributos e métodos.
São chamados de membros de classe, em oposição a membros de instância.
São Membros  funcionam independentemente de objetos, não precisam de objetos
para serem chamados. São chamados a partir do nome da classe
Aplicações Comuns :  classes utilitárias, Declaração de constantes
Uma classe que possui só membros estáticos pode ser uma classe estática também. Não poderá ser instanciada

Para cada objeto eu tenho um comportamento diferente quando temos membros de instancia

public static final double PI = 3.14 --> const usamos a palavra final

Depois do main colocamos as funções circumference e volume, podemos chamar elas no main. Deve ser estático se não o main não roda, porque ele é estático e só pode chamar métodos estáticos. 
Se não fosse estatico eu precisaria instanciar no main, e chamar o metodo com a instância. 

Operações de instancia são operações onde cada objeto tem o seu valor. Tipo para área de triangulo sabemos que cada triangulo teremos
um valor diferente. Já na calculadora as formulas sempre são as mesmas. 

No MAIN

``
    double radius = sc.nextDouble();
    double c = Calculator.circumference(radius);
    double v = Calculator.volume(radius);

    System.out.println(c);
    System.out.println("-");
    System.out.println(v);

``

## Construtores

Operação especial da classe que executa no momento da instanciação do objeto
Uso comuns : Iniciar valores dos atributos, permitir ou obrigar que o objeto receba dados, dependencias no momento de sua instanciação
A classe disponibiliza o construtor padrão --> Product p = new Product();

É possível especificar mais de um construtor na mesma classe --> sobrecarga

Quando instanciamos assim product = new Product estamos usando atributos vazios, ele recebe valores nulos e 0
Se queremos que o objeto obrigue o usuário a entrar com dados usamos o construtor.

Construtor para produto:

public  Produto(){
    this.name = name;
    this.price = price;
    this.qtd = qtd;
}

Palavra this --> referencia aos próprios atributos do objeto e passar o proprio objeto como argumento na chamada de método ou construtor. 

## Sobrecarga
*Lembre -se que em Java numeros já iniciam com 0.
Podemos colocar outros construtores recebendo menos parâmetros em Produto por exemplo.

## Encapsulamento
É um principo que consiste em esconder detalhes de implementaçao de uma classe, expondo apenas operações seguras
que mantenham objetos em estado consistente.

Regra: O objeto deve sempre estar em estado consistente e a propria classe deve garantir isso
UM OBJETO NÃO DEVE EXPOR NENHUM ATRIBUTO - padrao javabeans

``
class Produto{
private String name;  ---por ser private não pode ser acessado fora da classe
private double price; 
public String getName(){
return name;
}
public void setName(String name){
this.name = name
}
public double getPrice(){
return price;
}
public void setPrice(double price){
this.price = price;
}
}
``
No Main

``
System.out.println("Enter product name: ");
String name = sc.nextLine();
System.out.println("Enter product price: ");
double price = sc.nextDouble();
System.out.println("Enter quantity: ");
int qtd = sc.nextInt();
Produto product1 = new Produto(name, price, qtd);
System.out.println("Name: " + product1.getName());
product1.setPrice(35.00);
System.out.println("Price: " + product1.getPrice());
System.out.println("Quantity: " + product1.getQtd());
``
## Modificadores de Acesso
Private - o membro só pode ser acessado na mesma classe
Nada - só pode ser acessado nas classes do mesmo pacote
Protected - O membro só pode ser acessado no mesmo pacote e em subclasses de pacotes diferentes
Public - o membro é acessado por todas as classes

## Classes são tipos referências
Variáveis cujo tipo são classes não devem ser entendidas como caixas e sim como ponteiros para caixas
Variavel guarda endereço de memória onde objeto foi alocado. 
Tipos primitivos são tipos valor, são caixas que guardam a variável e não ponteiros

Quando alocamos usando new qualquer tipo estruturado, classe e array, são atribuidos valores padrão
aos seus elementos

numeros --> 0
boolean --> false
char --> '0'
objeto --> null

Tipos referencia são classes --> usufruem de todos recursos de OO --> variáveis são ponteiros.
Objetos precisam ser instanciadas usando new, ou apontar para objeto já existente
aceita valor null. Y=X --> Y aponta para onde X aponta. Obj instanciados no heap. Objetos não utilizados são desalocados em 
momento proximo pelo garbage collector

Tipos primitos são mais simples e performaticos. Variaveis são caixas. Não instancia, uma vez declarado estao prontos
Não aceitam valor Null. X=Y --> X recebe cópia de Y. Objetos são criados no stack. Objetos são desalocados imediatamnete
quando seu escopo é finalizado

## Desolocação de memória

Garbage collector --> automatiza gerenciamento de memória, no heap. Monitora os objetos no heap
que não estão sendo mais utilizados e desaloca.
Um objeto que está sem referencia é desalocado num futuro próprio. 

Variáveis que são de escopo somem automaticamente com o fim do escopo, não é o garbageCollector que age

## Vetores
Vetor é nome dado a arranjos unidimensionais. Arranjo é estrutura de dados homogenea, 
ordenada acessada por posições e estrutura é alocada de uma vez só em um bloco contíguo de memória

Vantagens --> Acesso imediato a elementos por sua posição
Desvantagens --> Tamanho fixo, dificuldade de inserção e deleção

``
int num = sc.nextInt();
double[] vect = new double[num];
for(int i = 0; i < num; i++){
vect[i] = sc.nextDouble();
}
double sum = 0.0;
int i = 0;
while(i<num)
{
sum += vect[i];
i++;
}
double avg = sum / num;
System.out.println("A média das alturas é: " + avg);
``

Quando meu vetor é do tipo referencia, ele cria ponteiros que deve apontar para objts que instanciamos
Primeiro devo instanciar o vetor inteiro, depois dentro do loop instancio cada item.

``
    Product[] vect = new Product[n];

        int i = 0;
        while(i < vect.length)
        {
            System.out.println("Digite o nome: ");
            String name = sc.nextLine();
            System.out.println("Digite o preço: ");
            double price = sc.nextDouble();
            vect[i] = new Product(name, price);
            i++;
        }
``
## Vetores multidimensionais


## Boxing
É o processo de conversão de objeto tipo valor para objeto de tipo ref compatível
int x = 20;
Object obj = x;

## Unboxing
É processo de conversao de obj tipo ref para obj tipo valor compativel

int x = 20;
Object obj = x;
int y = (int) obj

## Wrapper classes
classes equivalentes aos tipos primitivos. Cada tipo primitivo tem sua classe também, em letra maiuscula
Tem objetivo de tratar tipos como classe sem precisar de casting

int x = 20
Integer obj = 20;
int y = obj;

## Laço for each

Sintaxe opcional e simplificada para percorrer coleções
Para cada objeto nome, do grupo vect, imprima nome. 
for (String nome:vect) {
System.out.println(nome);}

## Listas
Estrutura de dados homogenea, ordenada, inicia vazia e seus elementos são alocados sob demanda
Cada elenmento ocupa um nó(nodo) da lista. 
Tipo(interface) : List
Classes que implementam: ArrayList, LinkedList
Cada nodo tem seu valor e ponteiro para próximo valor.
Vantagens: Tamanho variável, FAcilidade para se realizar inserções e deleções
Desvantagens: Acesso sequencial aos elementos. 

List<Integer> list; --> criar lista de inteiros do tipo generic Integer

- Add
Adiciona elementos na lista
``
  List<String> list = new ArrayList<>();
  list.add("Maria");
  for (String item:
  list) {
  System.out.println(item);
  }
  sc.close();
``
- Size --> tamanho da lista
- Remove --> list.remove("Maria") --> remover dado a partir da comparacao ou a posição
- removeif --> função lambda dentro de () --> retorna verdadeiro ou falso
list.removeIf(x => x.charAt(0) == 'M');
- list.indexOf --> fala o index do item que testo
- stream.filter -> x -> x.charAt(0) == 'A' . collect(collectors.toList()) --> operações de lambda para tipo string
``
  List<String> list = new ArrayList<>();
  list.add("Maria");
  list.add("João");
  for (String item:
  list) {
  System.out.println(item);
  }
  List<String> result = list.stream().filter(x -> x.charAt(0) == 'M').collect(Collectors.toList());
  for (String item:
  result) {
  System.out.println(item);
  }
``
- stream.filter(predicado).findFirst().orElse(null) -> coloca o primeiro elemento dentro de uma variável

## Matrizes
São arranjos bidimensionais. É um vetor de vetores
Arranjo (array) é estrutura de dados, homogenea, ordenada e ordenada em bloco contiguo de memoria uma vez só
Vantagens --> acesso imediato aos elementos de sua posição
Desvantagens --> tmanho fixo, dificuldade para se realizar inserções e deleções

Criar e instanciar:

int[][] matriz = new int[n][n];

``
int[][] matriz = new int[n][n];
for(int i = 0; i<n; i++)
{
for (int j = 0 ; j<n; j++)
{
System.out.println("digite um numero: ");
matriz[i][j] = sc.nextInt();
}
}
``

## Enumerações
É um tipo especial que serve para especificar de forma literal conjunto de consts
relacionadas
Usamos palavra ENUM
Vantagem --> Melhor semantica, codigo mais legível e auxiliado pelo compilador. 

Ex: Sistemas de comércio com pedidos e ciclo de vida. Pagamento pendente --> Processando --> enviado --> Entregue

``
Order order = new Order(1080, new Date(), OrderStatus.PENDING_PAYMENT);
``

Converter de String para Enum

OrderStatus os1 = OrderStatus.DELIVERED  ou OrderStatus.valueOf("DELIVERED");

## Design de Classes

Categorias de Classe --> Entidades, Serviços

## Composição
Relação tem um ou tem varios
Divide sistema em responsabilidades, coesão, flexibilidade, Reuso
Criamos a grande classe com atributos de tipos importados de outras
Caso tenhamos uma relação tem vários, teremos uma lista, não colocamos no construtor e sim instanciamos como ArrayList


## Herança

É um tipo de associação que permite que uma classe herde todos os dados e comportamento de outras
Vantagens: Reuso e polimorfismo


## Upcasting e Downcasting
- Upcasting casting da subclasse para superclasse, Uso comum em polimorfismo
- Downcasting é o casting da superclasse para subclasse. Uso comum em métodos que recebem parâmetros genéricos

``
//Upcasting --> Não da erro porque bcc é também do tipo account, ele usou extends
        Account acc1 = bcc;
``
Consigo atribuir objetos da subclasse a superclasse tranquilamente. Eles também são do tipo da superclasse

Agora o contrário eu não posso inverter diretamente. Devo forçar o tipo.

``
//Downcasting
BusinessAccount acc2 = (BusinessAccount) acc;
``

instanceOf --> descobrir se é instancia de determinada classe


## Sobreposição
Implementação de um método de uma superclasse na subclasse

é fortemente recomendável usar a anotação @Override em um método sobreescrito, Facilita a leitura e a compreensao
Avisamos ao compilador

## Super
é possível chamar a implementação da superclasse usando a palavra super. 
poderíamos chamar super.withdraw(amount) --> efetuo o mesmo código que já está na super classe

``
@Override
public void withdraw(double amount){
super.withdraw(amount);
balance = balance - 2;
}
``

## Classes e métodos final

Palavra final evita que a classe seja herdadade, em métodos evita que eles sejam sobrepostos

public final class SavingsAccount

o porque: depende da regra do negocio, as vezes é interessante garantir que a classe
não seja herdada. Geralmente convem acrescentar final em metodos sobrepostos, pois sobreposições
multiplas podem ser porta de entrada para inconsistências

Performance : atributos de tipo de classe final são analisados mais rápidos


## Polimorfismo

Polimorfismo é recurso que permite que variáveis de um mesmo tipo mais genérico possam apontar
para objetos de tipos diferentes, tendo assim comportamento diferentes conforme cada tipo. 
Associação do tipo especifico com tipo genérico é feita em tempo de execução(upcasting)
O compilador não sabe para qual tipo específico a chamada do método será feita, só na execução 


## Classes abstratas
São classes que não podem ser instanciadas. é uma forma de garantir herança completa
Vamos supor que no caso do banco, só existam contas para empresa e contas de savings, ou seja, não
existe conta comum. 

public abstract class Account 
na uml --> classe fica com nome em italico

Se a classe account não pode ser instanciada, pq não fazer só as outras -> 
Reuso --> Reutilizar atributos em diferentes classes sem precisar repetir
Polimorfismo --> A super classe genérica, nos permite tratar de forma fácil e uniforme todos os tipos de conta
Você pode colocar todos em uma mesma coleção

## Métodos Abstratos
Métodos que não possuem implementação. Métodos precisam ser abstratos quando sua classe é genérica demais para conter
a sua implementação. Se classe possui pelo menos método abstrato, a classe também é abstrato

Exemplo --> Na classe Shape, o método área depende do tipo da forma. Eu tenho que declarar para poder reusar e ter polimorfismo

No caso de Shapes, eu criaria uma list, botaria o add instanciando cada um das Shapes, dependeria de que forma seria e depois
poderia chamar cada item de list com shape.area(). Mesmo eu instanciando circle ou rectangle, ocorre um upcasting para shape
por que eu criei a list do tipo Shape:
List<Shape> list  =  new ArrayList<>()

## Tratamento de exceções

Qualquer condição de erro ou comportamento inesperado encontrado por programa em execução
Em java exceção é objeto herdado da classe -> java.lang.Exception (compilador obriga a tratar ou propagar) e
java.lang.RuntimeException que o compilador não obriga a tratar ou propagar

Quando lançaca, uma exceção é propagada na pilha de chamadas de métodos em exec, até que seja 
capturada(tratada) ou com o programa encerrado

Hierarquia de exceções do java -->
OutofMemoryError and VirtualMachineError --> programa que trata sozinho
Exception --> IOException RunTimeException

- Permite que errors sejam tratados de forma consistente e flexível usando boas práticas
- Delega a lpogica do erro para a classe responsável por conhecer as regras que podem ocasionar o erro
- Trata de forma organizada, exceções de tipos diferentes
- Pode carregar dados quaisquer

## Estrutura Try Catch
Bloco try --> contém código que representa a execução normal do trecho de código
que pode acarretar em uma exceção
Bloco catch --> contem código a ser executado caso uma exceção ocorra
DEve ser especificado o tipo da exceção, upcasting é permitido

try{

}
catch(ExceptionType e)
{

}

Eu não quero que meu programa pare de funcionar quando ocorre uma exceção, eu quero
que ele aconteça e o programa não pare. Precisamos capturar, passar mensagem de aviso.
O bloco try é onde colocamos funções que podem gerar exceção, no catch é onde passamos a mensagem
de erro. Assim o programa vai até o final

Tipos:
- arrayIndexOutOfBoundsException, InputMissMatchException ...


## Pilhas de chamadas de método
e.printStackTrace --> imprime a exceção, a sequencia de chamadas que gera a exceção

try{
}
catch( arrayIndexOutOfBoundsException e)
{
    system.out.println("Erro")
    e.printStackTrace
}

## Bloco Finally
é bloco que ocorre independente de ter ocorrido ou não exceção
Como por ex fechar arquivo, conexão de bd ou outro

try{
}
catch{
}
finally{
}

## Arquivos
Classe File, Scanner, IOException

File --> representação abstrata de arquivo e seu caminho

``
File file = new File("C:\\Users\\marbsouza\\Documents\\temp.txt");
Scanner sc = null;
try{
sc = new Scanner(file);
while(sc.hasNextLine()){
System.out.println(sc.nextLine());

        }
    } catch (FileNotFoundException e) {
        System.out.println("Error : " + e.getMessage());
        throw new RuntimeException(e);
    }
    finally {
        if(sc != null){
            sc.close();
        }
    }
    }
``

## File Reader e BufferedReader

File Reader --> Stream(sequencia) de leitura de caracteres a partir de arquivos
Buffered Reader --> Instanciado a partir do file reader, e implementa otimizações usando buff de memória

``
String path = "C:\\Users\\marbsouza\\Documents\\temp.txt";
FileReader fr = null;
BufferedReader br = null;

        try{
            fr = new FileReader(path);
            br = new BufferedReader(fr);
            String line = br.readLine();

            while (line != null){
                System.out.println(line);
                line = br.readLine();
            }
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
        finally {
            try {
                if (br != null) {
                    br.close();
                }
                if (fr != null) {
                    fr.close();
                }
            }
            catch(IOException e)
            {
                e.printStackTrace();
            }
        }
``

## Bloco Try-With-resources
Bloco try que declara um ou mais recursos e garante que esses recursos serão fechados no final do bloco
Eu não guardo o File Reader e BufferedReader dentro de variável, assim não preciso fechar

try(BufferedReader br = new BufferedReader(new FileReader(path)))

## FileWriter e BufferedWriter 

Stream de escrita de caracteres em arquivos
new FileWriter(path) --> cria recria arquivo
new FileWrite(path, true ) --> acrescenta arquivo existente

``

        String[] lines = new String[] {"Good morning", "Bye"};
        String path = "C:\\Users\\marbsouza\\Documents\\out.txt";

        try(BufferedWriter bw = new BufferedWriter(new FileWriter(path)))
        {
            for (String line: lines){
                bw.write(line);
                bw.newLine();
            }
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
``

Para não recriar e sim acrescentar:

``
new BufferedWriter(new FileWriter(path, true)
``

## Interfaces

Tipo que define conjunto de operações que uma classe deve implementar
Ela simplesmente define as abstrações. A gente só define a interface como uma classe abstrata, estabelece um contrato
que a classe deve cumprir. Ela nos ajuda a criar sistemas com baixo acoplamento e flexíveis

Facilita a nossa manutenção, assim precisamos alterar em apenas um lugar

Ex: RentalService depende do taxService genérico, e aí desacoplamos o sistema, e ai temos o BrazilTaxService
classe e ai depois se quisermos é só mudar essa ultima, e não precisaremos mudar no rental

Na hora de instanciar, qualquer classe que tenha sido implementada pela interface caberá no construtor. 


## Inversão de controle, Injeção de dependência

Quando fazemos associção direta de uma classe pra outra, tem um acoplamento forte e aí temos que alterar varios pontos
interfaces ajuda a diminuir acoplamento. A classe rentalService não conhece a dependência concreta

A injeção de dependencia pode ser pelo construtor por exemplo, igual falamos em cima. Temos um upcasting 
porque temos um TaxService mais genérico que vira BrazilTaxService que é mais específico

## Herdar X Cumprir Contrato

Em ambos o caso temos uma relação é um. Rectangle é um shape. BrazilTaxService é um TaxService
Temos tipos genéricos e especializados
Nesses casos temos polimorfismo, vindo de uma genérica e usando métodos específicos dependendo de qual objeto
foi instanciado em tempo de execução

Diferença: Herança temos reuso. Interface temos contrato a ser cumprido

Com shape não precisamos repetir color, area porque isso já vai. Em taxService não estou reaproveitando
nada. Eu só estou falando e obrigando que quem for implementado a partir de tal interface deverá ter os métodos 

Podemos misturar interface com classe. Uma classe é criada a partir de uma interface, podemos colocar novos atributos

## Herança multipla
Pode gerar o problema do diamante, uma ambiguidade causada pela
existência do mesmo método em mais de uma superclasse

Não é permitida na maioria das linguagens.

Uma solução é criar interfaces para serem implementadas. Assim o nosso objeto extende do objeto principal e depois
implementa outras interfaces. Não é herança multipla, apenas geramos contrato

## Interface Comparable
public interface Comparable<Tipo> {
int compareTo(Tipo o)
}

``
public static void main(String[] args) throws IOException {
List<String> list = new ArrayList<>();
String path = "C:\\Users\\marbsouza\\OneDrive - Globo Comunicação e Participações sa\\Documentos\\studies\\Java\\temp.txt";
try (BufferedReader br = new BufferedReader(new FileReader(path))){

    String name = br.readLine();
    while (name != null)
    {
        list.add(name);
        name = br.readLine();
    }
    Collections.sort(list);
    for (String s: list)
    {
        System.out.println(s);
    }

    }
    catch (IOException e)
    {
        System.out.println("Error: " + e.getMessage());
    }
``

Para usarmos o comparable, devemos implementar o contrato no objeto que desejamos comparar

## Default Methods

Também chamados de defend métodos, métodos concretos. Podemos usar a partir do Java 8
A intenção é prover a implementação padrão para métodos, de modo a evitar repetição de implementação
em toda classe que implemente a interface, a necessidade de se criar classes abstratar para prover reuso da implementação

Vantagens:
- manter a retrocompatibilidade com sistemas existentes
- Permitir que interfaces funcionais, que devem conter apenas um método, possam prover outras
operações padrão reutilizáveis

Interface não pode ter estados e nem construtores

## Generics

Permite que classes, interfaces e métodos possam ser parametrizados por tipo

-Reuso, type safety, performance

<>

## Tipos Curinga
Genéricos são invariantes, não posso atribuir list de uns tipos a list de outros. Não
conseguimos fazer upcasting

List <?> --> Compilador passa a aceitar a atribuição de diferentes tipos, consigo ler qualquer
tipo dentro da lista

Caso possível podemos usar <?> extends Shape por ex

## HashCode e Equals
Operações da classe object, utilziadas para comparar se objeto é igual a outro
equals é mais lento e mais correta

Tipo comuns já possuem implementação, classes personalizadas precisam sobreporlas

HashCode --> código que é gerado como num inteiro

Podemos gerar hashcode e equals em nossas classes automaticamente

## Set


## Spring Boot

- Anottations
- Framework para facilitar
- Spring web

Ordem da criação em classes:
- atributos básicos
- Associações
- Construtores
- Getters e SEtters
- HashCode e Equals
- Serializable -- Numero de Série . Podemos colocar implements Serializable do lado e pedir para gerar um numero de série
Ele transforma o objeto em bit para navegar na web

Application --> Camada Resource (rest controllers) --> Camada Serviço (regras de negocio onde depende de repository) --> Camada Acesso de Dados
Entidades

@RestController --> Recurso Web controlado por controlador Rest
@GetMapping --> Dizer que é para rodar o método Get.

Pom.xml --> ferramentas do build pelo Maven que usamos
Colocar dependencias para botar jpa e hw
Classe que salva dados repository
Classe de config

No spring para fazermos um objeto depender do outro, ele faz injeção de dependencia direto, Podemos só botar 
a anotation @autowired
