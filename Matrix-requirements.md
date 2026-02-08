<h1>Matrix requirements</h1>

*Matrix* is a command line program that realizes matrix computations.

Conventions:
- This file is written in Markdown format.
- Usage of regular meanings for `*`, `+`, `(`, `)` and `\` in regular expression.
- Requirements are formalized in this document with level 2 titles, as following:
  ```md
  ## <req-id>: <req-title>

  <req-text>
  ```
  `<req-id>` being the identifier of the requirement,
  `<req-title>` being the short title of the requirement,
  `<req-text>` being the full text of the requirement.


<!-- TOC -->

- [Interactive command line user interface](#interactive-command-line-user-interface)
    - [REQ-UI-010: Interactive command line interface](#req-ui-010-interactive-command-line-interface)
    - [REQ-UI-015: Prompt](#req-ui-015-prompt)
    - [REQ-UI-020: Left and right arrows](#req-ui-020-left-and-right-arrows)
    - [REQ-UI-030: HOME and END keys](#req-ui-030-home-and-end-keys)
    - [REQ-UI-040: BACKSPACE and DELETE keys](#req-ui-040-backspace-and-delete-keys)
    - [REQ-UI-050: ENTER key](#req-ui-050-enter-key)
    - [REQ-UI-060: Result messages](#req-ui-060-result-messages)
    - [REQ-UI-070: UI language](#req-ui-070-ui-language)
- [Command line syntax](#command-line-syntax)
    - [REQ-SYN-000: Empty and blank lines](#req-syn-000-empty-and-blank-lines)
    - [REQ-SYN-010: Variable assignment](#req-syn-010-variable-assignment)
    - [REQ-SYN-020: Matrix value](#req-syn-020-matrix-value)
    - [REQ-SYN-021: JSON matrix input](#req-syn-021-json-matrix-input)
    - [REQ-SYN-022: File matrix input](#req-syn-022-file-matrix-input)
    - [REQ-SYN-023: Variable value](#req-syn-023-variable-value)
    - [REQ-SYN-030: Parentheses](#req-syn-030-parentheses)
    - [REQ-SYN-040: + operator](#req-syn-040--operator)
    - [REQ-SYN-050: - operator](#req-syn-050---operator)
    - [REQ-SYN-060: * operator](#req-syn-060--operator)
    - [REQ-SYN-070: Operator priorities](#req-syn-070-operator-priorities)
    - [REQ-SYN-100: Stdout matrix output](#req-syn-100-stdout-matrix-output)
    - [REQ-SYN-110: File matrix output](#req-syn-110-file-matrix-output)
- [Design requirements](#design-requirements)
    - [REQ-DESIGN-010: Coding language](#req-design-010-coding-language)

<!-- /TOC -->


# Interactive command line user interface

## REQ-UI-010: Interactive command line interface

*Matrix* proposes an interactive command line interface.

## REQ-UI-015: Prompt

The command line interface introduces each line with the "Matrix> " text for prompt.

## REQ-UI-020: Left and right arrows

While editing a command line, the user may use the left and right arrows
to move the edition cursor inside the line being edited,
in order to insert characters within the line already started.

## REQ-UI-030: HOME and END keys

While editing a command line, the user may use the HOME and END keys,
to move the edition cursor at the beginning, resp. at the end,
of the line being edited.

## REQ-UI-040: BACKSPACE and DELETE keys

While editing a command line, the user may use the BACKSPACE and DELETE keys
to remove a character backward, resp. forward,
from the current position of the cursor inside the line being edited.

## REQ-UI-050: ENTER key

When the user presses ENTER,
the command line is analyzed according to the requirements in the next chapter

## REQ-UI-060: Result messages

When a non-empty nor blank line is processed,
a result message is displayed before the next prompt.

## REQ-UI-070: UI language

The language used in the command line interface is English (UK).


# Command line syntax

## REQ-SYN-000: Empty and blank lines

Empty and blank lines produce no effect.

## REQ-SYN-010: Variable assignment

The command line supports a ` *<var-name> *= *<matrix-value> *` syntax,
`<var-name>` describing a variable name as supported in Python,
`<matrix-value>` being a matrix value as per REQ-SYN-020.

## REQ-SYN-020: Matrix value

The command line supports matrix values as per:
- REQ-SYN-021: JSON matrix input
- REQ-SYN-022: File matrix input
- REQ-SYN-030: Parentheses
- REQ-SYN-040: `+` operator
- REQ-SYN-050: `-` operator
- REQ-SYN-060: `*` operator
- REQ-SYN-070: Operator priorities

## REQ-SYN-021: JSON matrix input

The command line supports matrix inputs as JSON data,
as supported in Python.

## REQ-SYN-022: File matrix input

The command line supports a `read\( *"<file-path>" *\)` syntax
to read a matrix from a JSON or a YAML file,
`<file-path>` describing the path (relative or absolute) of the file to read.

## REQ-SYN-023: Variable value

The command line supports a `<var-name>` syntax,
`<var-name>` being a variable name previously assigned with a REQ-SYN-010 line.

The resulting value is the matrix assigned to the variable.

## REQ-SYN-030: Parentheses

The command line supports a `\( *<matrix-value> *\)` syntax,
`<matrix-value>` being a matrix value as per REQ-SYN-020.

The usage of parentheses breaks regular operator priorities (REQ-SYN-070).

The resulting value is the result of the computation inside the parentheses.

## REQ-SYN-040: `+` operator

The command line supports a `<matrix-value> *\+ *<matrix-value>` syntax,
`<matrix-value>` being matrix values as per REQ-SYN-020.

The result is the matrix addition of the two matrixes.

## REQ-SYN-050: `-` operator

The command line supports a `<matrix-value> *- *<matrix-value>` syntax,
`<matrix-value>` being matrix values as per REQ-SYN-020.

The result is the matrix subtraction of the first matrix minus the second one.

## REQ-SYN-060: `*` operator

The command line supports a `<matrix-value> *\* *<matrix-value>` syntax,
`<matrix-value>` being matrix values as per REQ-SYN-020.

The result is the matrix product of the first matrix by the second one.

## REQ-SYN-070: Operator priorities

The list below gives operator priorities, from the most to the least prioritied:
1. `*`
2. `+` and `-`

Operators with the same priority are executed from left to right.

Examples:
- A * B + C * D <=> (A * B) + (C * D)
- A + B - C + D <=> ((A + B) - C) + D

## REQ-SYN-100: Stdout matrix output

The command line supports a ` *print\( *<matrix-value> *\) *` syntax,
`<matrix-value>` being a matrix value as per REQ-SYN-020.

The matrix value is printed out in the standard output,
as per REQ-SYN-021 (JSON matrix input), with the following constraints:
- one line per matrix row of the matrix,
- right alignment per matrix column of terms in each line.

## REQ-SYN-110: File matrix output

The command line supports a ` *write\( *<matrix-value> *,  *"<file-path>" *\) *` syntax,
`<matrix-value>` being a matrix value as per REQ-SYN-020,
`<file-path>` describing the path (relative or absolute) of the file to write.

Depending on the file extension,
a JSON or a YAML file is written.


# Design requirements

## REQ-DESIGN-010: Coding language

The language used in the source code is English (UK).
