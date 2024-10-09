import re #imports regular expression module

# replace "input" with file location
with open(r"C:\Users\deleo\CSC333-HW2\input.txt") as input_file:
    input_string = input_file.read()
print(input_file)

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    #for printing/debugging purposes
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokenize(input_text):
    tokens = [] #token list
    token_types = [
        ('Keyword', r'if|else|while|break|read|write|function|return'),
        ('Float', r'[0-9]+\.[0-9]?[0-9]?[0-9]?'),
        ('Integer', r'[0-9]+'),
        ('Addition', r'\+'),
        ('Subtraction', r'-'),
        ('Division', r'\/'),
        ('Multiplication', r'\*'),
        ('Power', r'\*\*'),
        ('Modulo', r'%'),
        ('Less_Than', r'>'),
        ('Greater_Than', r'<'),
        ('Not_Equal', r'!='),
        ('Equal', r'=='),
        ('Greater_Equal', r'>='),
        ('Less_Equal', r'<='),
        ('Assignment', r'='),
        ('And', r'&'),
        ('Or', r'\|'),
        ('Not', r'!'),
        ('Left_Parenthesis', r'\('),
        ('Right_Parenthesis', r'\)'),
        ('Left_Curly_Bracket', r'{'),
        ('Right_Curly_Bracket', r'}'),
        ('Semi_Colon', r';'),
        ('Comma', r','),
        ('Identifier', r'[A-Za-z_][A-Za-z0-9_]*'),
        ('Comment', r'#.*')
    ]

    # combines all regex types using '|' and creates fstring for each token type
    token_regex = '|'.join(f'(?P<{regex_type}>{regex_pattern})' for regex_type, regex_pattern in token_types)

    # iterates through input and adds identified tokens to tokens list
    for match in re.finditer(token_regex, input_text):
        input_regex_type = match.lastgroup
        value = match.group(input_regex_type)
        print(f"Token: {input_regex_type} -> {value}")
        tokens.append(Token(input_regex_type, value))
    print("All tokens: ")
    print(tokens)
    return tokens

# instance
tokens = tokenize(input_string)

# replace "output" with file location
with open('C:\\Users\\deleo\\CSC333-HW2\\output.txt', 'w') as output_file:
    for token in tokens:
        output_file.write(f"{token}\n")
print("Tokens now written")