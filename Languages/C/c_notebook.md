# C notebook

## Structure of a C program
- Documentation
- Link Section --> do the linking with other archives, #include <> ou #include "". That way we can use functions from outside
- Define Section --> Use to define constant and other variables
- Global Declaration Section --> Declare global variables
- Main section --> Only one for program
- Subprogram Section --> Where the function go

## Constants in C
Values that stay the same in all the program
Can be a Numeric or Character Constant. 
- After declared it can not change
- if is in '' is single character constant. If is in "" is String constant

## Datatypes in C

### Primary:

int- integer numbers. Can be positive and negative
float- float numbers with decimals
char- characters inside ''
double- more decimals numbers
void

### Derived:
- Array
- Structure
- Union
- Pointers

### User defined:
- type def
- Enumered DT


Size of type depends on the machine. But if int can support 4 bytes, it means 32 bits, 2^32 numbers tottaly
Int → 2 bytes
float → 4 bytes
double → 8 bytes
char → 1 byte

## Variables

To declare : 

type nome_da_variavel = valor;

At 42 school:

Declare before, and add after

type nome_da_variavel;
nome_da_variavel = valor;

## Operators in C

- Unary -, +, ++, --, !, &(adress), sizeof
- Binary &&, !!, !
- Ternary

Bitwise: &, |, ~ (bitwise not), ^ (bitwise xor), << (left shift), >> (right shift)  --> Performs in the byte level

A = 10  B = 5
A & B --> 1010 & 0101 --> 0000

## Formatted Input Function in C

Scanf() --> Use so the user can write and input data
Scanf("%d", &a);

## Formatted Output Functions in C

printf("expression", variable)
%d -> int
%s -> string
%c -> char

## If statements

Check conditions.

if (20>18)
{
printf(‘20 is greater than 18’)
}

## Ternary
(time < 18) ? printf(“Ok”) : printf(“Not ok”);

## Switch Statement

switch (expression)
{
	case x:
	break
	case y:
	break
	default:
	break
}
## While loops

 initialization
 while(condition)
 {
	body of loop
	update
 }

``
int i = 0
while (i<5)
{
	printf()
	i++
}
``

## Loops
- Entry
- Exit
- Counter / Condition

difference between for, while, do while --> in do while the condition is in the end, so the loop happens at least once.

While we can use when we don't no how many times the loop is going to happen.

for(int i = i; i < 10 ; i++)

## Do While

do{
	statement block
}
while(condition);

## Break statement

- way to get out of the loop
- the loop end at that time

## Continue statement

- just skip some statement and go to the next loop

## Nested loops

- repeting the repeting the process


while (condition)
{
	while(condition)
	{
		inner statement
	}
	outer statement
}

## Arrays in C

int a [5] --> can store five numbers integers
the index shows the position. Starts at 0

inicialization:

int a[5] = {0, -1, 11, 10, 2} --> correct
int a[] = {0, 2, 3, 4} --> correct
int a[5] = {0, -1, 3} --> correct, it
will place zeros in end
if i put more numbers its going to get error.

## 2D arrays

Arrays that need two loops and add two information

Datatype	namedArray [row_size] [column_size]


## Macros in C
We can define Macros before the program using Define. It's better to define constants and use the pre-processor to save time from the compile time and the execution time. 

Example:
``
#define SIZE 10
#define PRODUCT(X, Y) X * Y

int     main()
{
        int arr[SIZE];
        int a  = 3;
        int b = 5;
        printf("%d", PRODUCT(a,b));
}
``


# Makefile
Describe how a program should be build.
You can add rules with targets and the code i should run to execute de rule, example:

hello : hello.c
        gcc -o hello hello.c

You can use the rule 'all' to run all the rules, use variables using caps letters and '=' to atributte values. Then just use $() to use the variables, example:

CC=gcc
hello : hello.c
        $(CC) -o hello hello.c

clean : 
        rm hello test.o

