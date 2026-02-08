<h1>Matrix test plan</h1>

Test plan for *Matrix*.

Based on [Matrix-requirements.md](./Matrix-requirements.md).

Conventions:
- This file is written in Markdown format.
- Tests are formalized in this document with level 2 titles, as following:
  ```md
  ## <req-id>(/<req-id>)*: <test-title>

  <test-text>
  ```
  `<req-id>` giving the requirement identifiers covered,
  `<test-title>` being the short title of the test,
  `<test-text>` being the full text of the test, described with "Action"s and "Expected result"s.


<!-- TOC -->

- [Interactive command line user interface](#interactive-command-line-user-interface)
    - [REQ-UI-010/REQ-UI-015: Interactive command line interface](#req-ui-010req-ui-015-interactive-command-line-interface)
    - [REQ-UI-050/REQ-UI-060/REQ-UI-070: Result messages & UI language](#req-ui-050req-ui-060req-ui-070-result-messages--ui-language)
    - [REQ-UI-020/REQ-UI-030/REQ-UI-040: Current line editing](#req-ui-020req-ui-030req-ui-040-current-line-editing)
- [Command line syntax](#command-line-syntax)
    - [REQ-SYN-000: Empty and blank lines](#req-syn-000-empty-and-blank-lines)
    - [REQ-SYN-010: Variable assignment](#req-syn-010-variable-assignment)
    - [REQ-SYN-100: Stdout matrix output](#req-syn-100-stdout-matrix-output)
    - [REQ-SYN-020: Matrix value](#req-syn-020-matrix-value)
    - [REQ-SYN-021: JSON matrix input](#req-syn-021-json-matrix-input)
    - [REQ-SYN-022: File matrix input](#req-syn-022-file-matrix-input)
    - [REQ-SYN-110: File matrix output](#req-syn-110-file-matrix-output)
    - [REQ-SYN-023: Variable value](#req-syn-023-variable-value)
    - [REQ-SYN-040: + operator](#req-syn-040--operator)
    - [REQ-SYN-050: - operator](#req-syn-050---operator)
    - [REQ-SYN-060: * operator](#req-syn-060--operator)
    - [REQ-SYN-070: Operator priorities](#req-syn-070-operator-priorities)
    - [REQ-SYN-030: Parentheses](#req-syn-030-parentheses)
- [Design requirements](#design-requirements)
    - [REQ-DESIGN-010: Coding language](#req-design-010-coding-language)

<!-- /TOC -->


# Interactive command line user interface

## REQ-UI-010/REQ-UI-015: Interactive command line interface

Action: Launch the program.

Expected result: The program displays the "Matrix>" prompt.


## REQ-UI-050/REQ-UI-060/REQ-UI-070: Result messages & UI language

Action: Type any valid command line, then ENTER.

Expected result: The command line result is printed out. The language used is English.


## REQ-UI-020/REQ-UI-030/REQ-UI-040: Current line editing

Action: Start typing a line, then use left and right arrows, HOME and END keys, BACKSPACE and DELETE keys.

Expected result: The current command line can be edited from where the cursor is currently located.


# Command line syntax

## REQ-SYN-000: Empty and blank lines

Action: Type ENTER.

Expected result: The program just displays the "Matrix>" prompt again.


## REQ-SYN-010: Variable assignment

Action: Type `A = [[0]]`.

Expected result: The assignment succeeds.

Action: Type `print(A)`.

Expected result: The program displays the value of A.


## REQ-SYN-100: Stdout matrix output

Action: Type
```
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(A)
```

Expected result: The program display the matrix with 3 columns aligned and 3 rows.


## REQ-SYN-020: Matrix value

Action: Check the tests for the following requirements all pass:
- REQ-SYN-021: JSON matrix input
- REQ-SYN-022: File matrix input
- REQ-SYN-030: Parentheses
- REQ-SYN-040: `+` operator
- REQ-SYN-050: `-` operator
- REQ-SYN-060: `*` operator
- REQ-SYN-070: Operator priorities


## REQ-SYN-021: JSON matrix input

Action: Type `A = [[0]]`.

Expected result: The assignment succeeds.

Action: Type `print(A)`.

Expected result: The program displays the value of A with a single column and a single row.

Action: Type `A = [[0, 1]]`.

Expected result: The assignment succeeds.

Action: Type `print(A)`.

Expected result: The program displays the new value of A with two columns and a single row.

Action: Type `A = [[0, 1], [2, 3]]`.

Expected result: The assignment succeeds.

Action: Type `print(A)`.

Expected result: The program displays the new value of A with two columns and two rows.


## REQ-SYN-022: File matrix input

Action: Type `A = read("A.json")`.

Expected result: The assignment succeeds.

Action: Type `print(A)`.

Expected result: The program displays the value of A with two columns and two rows.


## REQ-SYN-110: File matrix output

Action: Type `A = read("A.json")`.

Expected result: The assignment succeeds.

Action: Type `write(A, "/tmp/A.json")`.

Expected result: The program succeeds at saving the `/tmp/A.json` file.

Action: Check the content of the `/tmp/A.json` file.

Expected result: The content of the file is the same as the original `A.json` file.


## REQ-SYN-023: Variable value

Action: Type `A = read("A.json")`.

Expected result: The assignment succeeds.

Action: Type `print(A)`.

Expected result: The program displays the content of A.

Action: Type `A2 = A`.

Expected result: The assignment succeeds.

Action: Type `print(A2)`.

Expected result: The program displays the same content as for A.


## REQ-SYN-040: `+` operator

Action: Type
```
A = read("A.json")
B = read("B.json")
Addition = A + B
print(Addition)
```

Expected result: The program displays
```
2 4
6 8
```


## REQ-SYN-050: `-` operator

Action: Type
```
A = read("A.json")
B = read("B.json")
Subtraction = A - B
print(Subtraction)
```

Expected result: The program displays
```
0 0
0 0
```


## REQ-SYN-060: `*` operator

Action: Type
```
A = read("A.json")
B = read("B.json")
Product = A * B
print(Product)
```

Expected result: The program displays
```
 7 10
15 22
```

Action: Type
```
A = read("A.json")
C = read("C.json")
Product = A * C
print(Product)
```

Expected result: The program displays
```
1
3
```

Action: Type
```
B = read("B.json")
D = read("D.json")
Product = B * D
print(Product)
```

Expected result: The program displays
```
6
8
```


## REQ-SYN-070: Operator priorities

Action: Type
```
A = read("A.json")
B = read("B.json")
C = read("C.json")
D = read("D.json")
R = A * C + B * D
print(R)
```

Expected result: The program displays
```
 7
11
```

Action: Type
```
A = read("A.json")
B = read("B.json")
R = A + B - A + B
print(R)
```

Expected result: The program displays
```
10 12
14 16
```


## REQ-SYN-030: Parentheses

Action: Type
```
A = read("A.json")
B = read("B.json")
D = read("D.json")
R = A + B * D
```

Expected result: The computation fails because the number of columns mismatch.

Action: Type
```
A = read("A.json")
B = read("B.json")
D = read("D.json")
R = (A + B) * D
print(R)
```

Expected result: The program displays
```
 8
12
```


# Design requirements

## REQ-DESIGN-010: Coding language

Action: Check the source code.

Expected result: The source code is written in English language.
