# Python Interpreter

This project features a Python interpreter for a custom programming language, designed to parse and interpret a specific grammar set.

## Features

- Parses and interprets a defined grammar including assignments, conditional statements, loops, and function definitions.
- Supports arithmetic and boolean expressions, and basic input/output operations.

## Grammar

The grammar supported by this interpreter includes:

prog     : block
block    : stmt ';' block
         | stmt
stmt     : assn
         | 'rd' id
         | 'wr' expr
         | 'if' boolexpr 'then' stmt
         | 'if' boolexpr 'then' stmt 'else' stmt
         | 'while' boolexpr 'do' stmt
         | 'begin' block 'end'
assn     : id '=' expr
expr     : term addop expr
         | term
term     : fact mulop term
         | fact
fact     : id 
         | num
         | '(' expr ')'
         | '-' fact
boolexpr : expr relop expr
addop    : '+'
         | '-'
mulop    : '*'
         | '/'
relop    : '<'
         | '<='
         | '>'
         | '>='
         | '<>'
         | '=='


## Prerequisites

- Python installed on your system.
- Access to a terminal or command prompt.

## Installation

1. Clone the repository or download the script to your local machine.
2. Navigate to the directory containing the script.

## Usage

To run the interpreter, open your terminal and execute the following command:

```bash
python3 interpreter.py "your_program"

For example, running the following will read in two numbers from the user. Input numbers "15" and "25" after running, and the GCD of the two numbers will be calculated (5):
python3 interpreter.py "rd a; 
>> rd b;
>> while a<>b do
>>     if a>b then
>>         a=a-b
>>     else
>>         b=b-a;
>> wr a"
