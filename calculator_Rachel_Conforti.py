#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cjeffcoa
@author: Rachel Conforti
"""

import math


def basic():
    # =============================================================================
    #     +     for a + b
    #     -     for a - b
    #     /     for a / b
    #     *     for a * b
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Incorrect operator! Please select from the given options!"


def scientific():
    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')


    if op in '^r%':
        a = int(input('Please type the first number: '))
        b = int(input('Please type the second number: '))
        # If you choose power it will go in here. If not it will skip this f statement.
        if op == "^":
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(math.pow(a, b))
        # IF you choose to do a root it will enter. If not go to the next.
        # CAN ONLY DO ONE NUMBER THAT OKAY?
        if op == "r":
             return str(a) + ' ' + op + ' = ' + str(math.sqrt(a))
        # If you choose to do a remainder it will enter below. If not it will go to the next.
        if op == "%":
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(math.remainder(a, b))
    elif op in '!sincostanln':
        a = int(input('Please type the number: '))
        # If you choose factorial.
        if op == "!":
            return str(a) + op + ' = ' + str(math.factorial(a))
        # If you choose sin.
        if op == "sin":
             return op + "(" + str(a) + ")" + ' = ' + str(math.sin(a))
        # If you choose cos.
        if op == "cos":
            return op + "(" + str(a) + ")" + ' = ' + str(math.tan(a))
        # If you choose natural log.
        if op == "ln":
            return op + "(" + str(a) + ")" + ' = ' + str(math.log(a))
    else:
        return "Invalid choice. Choose again."
        # Your solution here


def main():  # Wrapper function

    print("""Choose a calculator
    1. Basic Calculator
    2. Scientific Calculator""")
    choice = int(input('Please choose as 1 or 2: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    else:
        print('Invalid choice! Please select between 1 and 2:')


if __name__ == '__main__':
    main()