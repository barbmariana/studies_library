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

int marks[][10];

int a[2][3] = {{0,0,0}, {1, 1, 2}}
int a[2][3]={
	{},
	{}
}


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

## Strings

## Linked List

- one space to variable and one that saves a pointer to the next node

``
Struct node
{
	int a,
	struct node * next,
}
``

-Singly LL - 2 bytes, Data and adress(adress next node)
- Doubly LL
- Circular LL
- Doubly Circular LL

Singly LL:
Data | adress(pointer next)

Doubly LL:
Two pointers to previous and next;
First and last have null adress;

struct node
{
	int data;
 	struct node * next;
  	struct node * prev;
}

## Header files
- code that we like to share with other code
- put a declaration of a function that i'd like to use so my program will know where to find
- even though i have the declarations in the header file, i must have all the compile files to do the correct linking. Just the linking wont be enough to run the program. So if you have a program that calls other functions you need all of them compiled
- if you just include the funcion in your program, you dont need to compile it manually, but this is not a good practice because everytime you change a function everything will be recompile and imagine having so many includes it will not be good for organization


#ifndef
#define
#endif


## Makefile
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


## Signals in Linux

Library : signal.h
signaction --> type to create handlers
We can use a handler to change a signal function by using signal(SIGUSR, handler)

SIGINT - ctrl + c
SIGIGN - ignore signal
SIGKILL - kill terminal kill(target process id, signal number)
CMD --> kill -TERM <PID>
sleep(1) --> take a moment to continue

Signals are a notification to a process that an event has occurred. It can be send by some actions as hardware exception ocurred, the typed characters by the user, a software event occurred. 

Signals are defined as a unique integer, but we know then by their symbolic names. 

First a signal is generated by some event --> Signal is delivered to a process --> process takes some action in response

### Signal Handler
Is a funcion that performs appropriate tasks in response to delivery of a signal. The shell itself has a response for ctrl + c to end the process. 

To change the signal dispositions, we can use SIGNAL() and SIGACTION().

signal --> original api to setting the disposition of a signal and it provides a simpler iterface than sigaction().

`` 
#include <signal.h>

void ( *signal(int sig, void (*handler)(int)) ) (int);

``
The first argument, sig, identifies the signal whose disposition we wish to change. The second argument, handler, is the address of the function that should be called when this signal
is delivered. 

``
void
handler(int sig)
{
 /* Code for the handler */
}
``

We can make the prototype for signal() much more comprehensible by using the
following type definition for a pointer to a signal handler function:

``
typedef void (*sighandler_t)(int);
This enables us to rewrite the prototype for signal() as follows:
sighandler_t signal(int sig, sighandler_t handler)
``

Invocation of a signal handler may interrupt the mains program flow at many time. the kernel calls the handler on the process's behalf and the handler returns execution of the program resumes at the point where the handler interrupted it. 

We can establish the same handler to
catch different types of signals and use this argument to determine which signal
caused the handler to be invoked.


### Socket
Used for communication in Client-Server Systems. Is a endpoint for communication.

Is indetified by an IP address concatenated with a port number