"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    token = raw_input("> ")
    token = token.split()
    operator = token[0]

    if operator == "q":
        break
    elif operator == "+":
        print add(float(token[1]), float(token[2]))
    elif operator == "-":
        print subtract(float(token[1]), float(token[2]))
    elif operator == "*":
        print multiply(float(token[1]), float(token[2]))
    elif operator == "/":
        print divide(float(token[1]), float(token[2]))
    elif operator == "square":
        print square(float(token[1]))
    elif operator == "cube":
        print cube(float(token[1]))
    elif operator == "pow":
        print power(float(token[1]), float(token[2]))
    elif operator == "mod":
        print mod(float(token[1]), float(token[2]))
