# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:45:00 2023

@author: Brittany
"""

from flask import Flask, render_template, request, redirect, url_for, session

# Initialize memory bank
memory = 0

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

# Menu to select operation, main calculator loop
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Memory Recall")
    print("6. Clear Memory")
    print("7. Enter Problem for Student")
    print("8. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice == '8':
        print("Calculator exiting...")
        break

    try:
        if choice == '7':
            problem = input("Enter a math problem for the student: ")
            try:
                # Evaluate the entered expression
                result = eval(problem)
                print("Result:", result)
                memory = result
            except:
                print("Invalid math problem. Please enter a valid expression.")
            continue
        elif choice != '5':
            # inputs for basic operations
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numerical value.")
        continue

    # Perform selected operation based on user's choice.
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = memory
        print("Memory Recall:", result)
    elif choice == '6':
        memory = 0
        print("Memory Cleared.")
        continue
    else:
        print("Invalid choice")
        continue

    # Display result and update memory
    print("Result:", result)
    memory = result