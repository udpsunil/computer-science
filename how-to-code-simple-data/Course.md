# 0: Introduction
## Welcome
### Systematic Program Design
* What the program is supposed to do?
* What are the smallest steps needed to complete the program?
#### Methodology
* BSL is used to learn the language in 1 week
* Next learn the design over rest of the course duration.
# 1a: Beginning Student Language
## Expressions
(<primitive> <expression> ...)
* sqr - Function to Square
* sqrt - Function to perform Square Root
* comment box
* sqrt of 2 is irrational. meaning it takes infinite size to represent the
  number. This means racket is not able to show entire number. It is shown as
  #i1.4142135623730951 (sqrt 2)
## Evaluation
* Step by step rules for evaluating an expression.
* primitive call is the operator (like '+') and operands follow the operator.
* Rule 
    * Left to Right evaluation
    * All operands needs to be reduced to values
    * Then apply primitive to the values
## Strings and Images
* string-append - append strings
* string-length - length of strings
* substring - gives sub string from start to end 
* Images
    * (require 2htdp/image)
    * circle: radius, solid, red
    * rectangle: length, width, "outline", "blue"
    * text: string, size, color
    * above: append images one above another
    * beside: same as above but stacks next to one another
    * overlay: same as above but stacks on top of one another
