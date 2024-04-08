# Java Alura

- para rodar o main precisamos do public static void main(String[] args{})

## Variables

formato:

tipo    nomeVariável = valor;

## Operadores

+, - . *, /, %(modulo)
== igual
!= diferente
> < >= <=

Tipos lógicos:

&& and
|| or
! not

## Convenções

- Nome de classes começam com letra maiuscula, PascalCase
- Metodos e variáveis são letras minusculas, CamelCase
- Constantes são em letras totalmente maiusculas

## Tipos

- boolean : valores lógicos, true e false
- byte - valores numéricos de -127 a 128
- char - caracter unicode aspas duplas
- short - valores de 16 bits
- int - valores de 32 bits
- long - valores de 64 bits
- float - valores de pontos flutuantes
- double - valores de pontos flutuantes de dupla precisao

## Trabalhando com textos

- Podemos concatenar
- usar valor String importado
- Text blocks dentro de """ """
- Método formatted - usamos o .formatted em um texto para colocar variaveis
".... %s".formatted(nome, aulas)

Comparação entre Strings:

- Não da para utilizar o == e esperar que de totalmente certo por que ele checa o espaço na memória
- Podemos usar o .equals()

senha.equals(teste);

## Casting

(int) expressão
colocamos o tipo dentro do parenteses

## Condicional

if() 
{

}
else if()
{

}
else
{

}

## Leitura de dados

Usamos a classe Scanner

- Scanner sc = new Scanner(System.in)
- Ele fica de olho no teclado para pegar o que for digitado
- toLocale

String filme = sc.nextLine();

NextInt() -> pega um numero

## Loops

- While(booleana) - usado quando não sabemos a quantidade de laços

- Número aleatório : Random.nextInt()

- For - quando sabemos o numero de operações

for( int i = 0; i < ; i++)

## Programação Orientada a Objetos

- Classes são moldes de objetos que podem ter diversos atributos e métodos

- Atributos : são os valores que caracterizam os métodos
- Métodos : são as ações disponíveis

tipo nomeAtributo;
tipo nomeAtributo2;

void    metodo()
{

}

Criar objetos:

- Para criar o objeto a partir da classe fazemos a instanciação

tipoClasse nomeObjeto = new tipoClasse(aqui ou podemos colocar todos os atributos ou podemos ir colocando um por um, depende do constructor)

Constructor:

``
    public Movie(String name, int releaseYear, boolean streamInclused, double score, int evaluationTotal, int movieDuration) {
        this.name = name;
        this.releaseYear = releaseYear;
        this.streamInclused = streamInclused;
        this.score = score;
        this.evaluationTotal = evaluationTotal;
        this.movieDuration = movieDuration;
    }
``

Associando valor ao atributo:

Pessoa pessoa1 = new Pessoa();

pessoa1.nome = "Ana";
pessoa1.idade = 20;

## Modificadores de Acesso e visibilidade

- Private : O valor pode ser atribuído apenas na própria classe. Outras classes não conseguem mudar o valor a menos que utilizem métodos getters e setters

- Public : O valor pode ser acessado e atribuído por qualquer classe

- Protected

- Default : O modificador de acesso default é aquele que não especifica nenhum modificador de acesso. Quando nenhum modificador de acesso é especificado, a classe, atributo ou método pode ser acessado apenas pelas classes que estão no mesmo pacote.

## Métodos que acessam e modificam

- getters : Criar métodos de acesso para os atributos
- setters: Criar métodos de modificação e atribuição de atributos

## Diferença entre herança e interface

- Em Java só podemos herdar de uma classe
- Podemos implementar outras interfaces
- Classes herdam atributos e métodos, já interface é apenas métodos
- A interface é um contrato que fazemos que a nossa classe que a implementar tera os métodos
- Interfaces apenas obrigam o programador a seguir o padrão do projeto
- Classe quer dizer que sou daquele tipo. Já interface quer dizer que posso me comportar daquela forma quando necessário. 

## Java Collections

- var : realiza inferencia do tipo
- Na hora de criar  podemos definir o tipo que aceite diferentes tipos de objeto, apenas podemos colocar a classe mãe


- ArrayList<TipoDosDAdos> nome = new ArrayList<>():
        - add() - adiciona
        - size() - tamanho
        - get(posicao).getNone();
        - toString() - Podemos reescrever, com um Override


- Array : 
        - int[] nome = new int[tamanho]

## Método Construtor

- Estou construindo de fato um objeto
- Posso passar parâmetro ou não
- Construtores vazios ou com argumentos
- recebe o mesmo nome da classe

public Filme (string nome, int ano)
{
        this.setNome(nome);
        this.nome = nome;
}

Com classes herdeiras:

public Setie(String nome, int ano)
{
        super(nome, ano);
}

## InstanceOf

- podemos utilziar para verificar se objeto é instancia de determinada classe

if (item instanceof Filme file){
        sout(filme.getClassificacao)
}

Se eu pego um objeto e aponto para outro, ele está fazendo uma referencia apenas e não copiando ele. Assim se você mudar algo nele mudara no objeto original

## Ordenando Dados

Podemos ordernar array de strings, numeros:

Collections.sort(lista) -> ordenar array de strings


Para casos onde os objetos não sabem se comparar um com outro, precisamos nós implementar essa interface em nossos objetos. 

Na classe colocamos:

classe implements Comparable

public int compareTo(Titulo outro)
{
        return this.getNome().compareTo(outro.getNome());
}

ou

lista.sort(Comparator.comparing(Titulo:: getAnoDeLancamento));


### Interface List

Existem diversos tipos de interface com diversos métodos. 

- LinkedList<>();
- Interface Map<K, V> - Chave valor

Podemos substituir o tipo para a interface List que é o tipo mais genérico e aceita todos:

List<Titulo> lista = new ArrayList<>();

Map<String, Integer> usandoHashMap = new HashMap<>();

        usandoHashMap.put("Gatos", 1);
        int valor = usandoHashMap.get("Cachorros");
        usandoHashMap.remove("Gatos");
for (String chave : usandoHashMap.keySet()) {
            System.out.println("Chave: " + chave);
            System.out.println("Valor: " + usandoHashMap.get(chave));
        }