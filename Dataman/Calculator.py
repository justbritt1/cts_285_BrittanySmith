# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Creating a calculator to add, subtract, multiply, and divide.
# Brittany Smith / Justin Graves
# M1T1
# 8/23/2023
"""
Created on Tue Aug 22 13:37:51 2023

@author: smithb8349
"""

# Functions for add, subtract, multiply, divide.

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
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Calculator exiting...")
        break
    
    try:
        # Non-numeric inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numerical value. ")
        continue
    
    # Perform selected operation based on user's choice.
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")