# CSC333-LanguagesAndMachines

CSC 333: Assignment 2

In this assignment, we were tasked with providing the software implementation of a lexical analyzer for a simplified langauge. As output, it should print a list of the token type and its value, in order of the input tokens. Any lexical errors should be labeled properly with a message.

The instructions are below.

The simplified language supports the following:

Numbers including both integer and floating-point (3-point precision after decimal): 0, 1000, 233, 0.005, 1.23
Numeric Operators: Addition (+), Subtraction (-), Division (/), Multiplication (*), Power (**), Remainder or Modulo (%)
Relational Operators: Less (<), Greater (>), Not Equal (!=), Equal (==), Greater Equal (>=), Less Equal (<=)
Assignment Operator: (=)
Logical Operators: And (&), Or (|), Not (!)
Other Operators: Left Parenthesis ({), Right Parenthesis (}), Left Bracket ((), Right Bracket ()), Semi-colon (;), Comma (,)
Identifiers (can contain alphabets, numbers, and special character underscore _ but must start with a letter or underscore _): examples include i, j, index, a123
Keywords: if, else, while, break, read, write, function, return
Comments: Any number of characters preceded by # until a newline is reached
The tokenizer does not know anything about the meaning or syntax of expressions. It uses white space (space and tab characters and the end of line) to determine where tokens end or begin. Since white space has no meaning in the expression, no tokens are generated for white space and comments. (Similarly, in the Python interpreter, comments are removed by the tokenizer.)

For example:

123456 and 123 456 result in different token sequences, and so do i22 and i 22.
On the other hand, both i22!=0 and i22 != 0 result in the same sequence of tokens (namely identifier i22, not equal operator !=, number 0).
Example input file:

kotlin
Copy code
{
    while (i < 0) {i = anIdent234 12
    if i22!=0 return 4;
}
Example output:

vbnet
Copy code
Token: LPar({)
Token: Keyword(while)
Token: LBrac(()
Token: Identifier(i)
Token: LThan(<)
Token: Integer(0)
Token: RBrac())
Token: LPar({)
Token: Identifier(i)
Token: Assignment(=)
Token: Identifier(anIdent234)
Token: Integer(12)
Token: Keyword(if)
Token: Identifier(i22)
Token: NotEqual(!=)
Token: Integer(0)
Token: Keyword(return)
Token: Integer(4)
Token: Semicolon(;)
Token: RPar({)
Code instructions:

Your code must be in either Python or C++. It should be modularized and properly documented. Please include the programming language version and details necessary to compile (for C++ code) and run the program.
Your code should be able to take input from a file.
Your output should be shown in the output terminal and saved in a file.