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
    



# replace "output" with file location
output_file = open('C:\\Users\\deleo\\OneDrive\\Desktop\\CSC333 HW2\\output.txt', 'w')
#output_file.write("This writes into the file")
#output_file.close()

