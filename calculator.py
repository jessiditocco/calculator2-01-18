"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    token = raw_input("> ")
    token = token.split(" ")

    if token[0] == "q":
        break
    elif token[0] == "+":
        print add(float(token[1]), float(token[2]))
    elif token[0] == "-":
        print subtract(float(token[1]), float(token[2]))
    elif token[0] == "*":
        print multiply(float(token[1]), float(token[2]))
    elif token[0] == "/":
        print divide(float(token[1]), float(token[2]))
    elif token[0] == "square":
        print square(float(token[1]))
    elif token[0] == "cube":
        print cube(float(token[1]))
    elif token[0] == "pow":
        print power(float(token[1]), float(token[2]))
    elif token[0] == "mod":
        print mod(float(token[1]), float(token[2]))
        