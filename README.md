# Python Interpreter

This project features a Python interpreter for a custom programming language, designed to parse and interpret a specific grammar set.

## Features

- Parses and interprets a defined grammar including assignments, conditional statements, loops, and function definitions.
- Supports arithmetic and boolean expressions, and basic input/output operations.

## Grammar

The grammar supported by this interpreter includes:

```plaintext
prog     : block
block    : stmt ';' block | stmt
stmt     : assn | 'rd' id | 'wr' expr | 'if' boolexpr 'then' stmt | 'if' boolexpr 'then' stmt 'else' stmt | 'while' boolexpr 'do' stmt | 'begin' block 'end' | 'def' id '(' id ')' '=' expr
assn     : id '=' expr
expr     : term addop expr | term bitop expr | term
term     : fact mulop term | fact
fact     : id | num | '(' expr ')' | '-' fact | id '(' expr ')'
boolexpr : expr relop expr
addop    : '+' | '-'
mulop    : '*' | '/'
relop    : '<' | '<=' | '>' | '>=' | '<>' | '=='
