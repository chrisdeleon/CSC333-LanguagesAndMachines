import re #imports regular expression module

# replace "input" with file location
input_file = open(r"C:\Users\deleo\OneDrive\Desktop\CSC333 HW2\input.txt")
#print(input_file.read())

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    #for printing/debugging purposes
    def __repr__(self):
        return f"Token({self.type}, {self.value})"
    

def tokenize(input):
    tokens = [] #token list

    token_types = [
        ('Integer', r'[0-9]*'),
        ('Float', r'[0-9]+.[0-9]?[0-9]?[0-9]?'),
        ('Addition', r'\+'),
        ('Subtraction', r'-'),
        ('Division', r'\/'),
        ('Multiplication', r'\*'),
        ('Power', r'\*\*'),
        ('Modulo', r'%'),
        ('Less Than', r'>'),
        ('Greater Than', r'<'),
        ('Not Equal', r'!='),
        ('Equal', r'=='),
        ('Greater Equal', r'>='),
        ('Less Equal', r'<='),
        ('Assignment', r'='),
        ('And', r'&'),
        ('Or', r'\|'),
        ('Not', r'!'),
        ('Left Parenthesis', r'\('),
        ('Right Parenthesis', r'\)'),
        ('Left Curly Bracket', r'{'),
        ('Right Curly Bracket', r'}'),
        ('Semi Colon', r';'),
        ('Comma', r','),
        ('Identifier', r'[A-Za-z_][A-Za-z0-9_]*'),
        ('If', r'if'),
        ('Else', r'else'),
        ('While', r'while'),
        ('Break', r'break'),
        ('Read', r'read'),
        ('Write', r'write'),
        ('Function', r'function'),
        ('Return', r'return'),
        ('Comment', r'#.*')
    ]

# replace "output" with file location
output_file = open('C:\\Users\\deleo\\OneDrive\\Desktop\\CSC333 HW2\\output.txt', 'w')
#output_file.write("This writes into the file")
#output_file.close()