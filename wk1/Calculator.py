# Calculator.py
"""calculates the sum, difference, modulus, product or quotient of two integers"""

# Welcome prompt
print("Welcome to the Python Calculator Application.")
print("What calculation do you want to perform?")
print("1) Addition (+)\n2) Subtraction (-)\n3) Division (/)")
print("4) Multiplication (*)\n5) Modulus (%)")
print()
initialPrompt = int(input("Enter 1,2,3,4 or 5 indicating your selection: "))
    
# if statements for each menu choice
if initialPrompt == 1:
    print("You have selected addition.")
    input1 = int(input("Enter your first integer: "))
    input2 = int(input("Enter your second integer: "))
    print("\nThe addition of",input1,"and",input2,"is",(input1+input2))
    
if initialPrompt == 2:
    print("You have selected subtraction.")
    input1 = int(input("Enter your first integer: "))
    input2 = int(input("Enter your second integer: "))
    print("\nThe subtraction of",input1,"and",input2,"is",(input1-input2))
    
if initialPrompt == 3:
    print("You have selected division.")
    input1 = int(input("Enter your first integer: "))
    input2 = int(input("Enter your second integer: "))
    # additional if statements since divisor cannot be zero
    if input2 == 0:
        print("Cannot divide by zero.")
    if input2 != 0:
        print("\nThe division of",input1,"and",input2,"is",(input1/input2))

if initialPrompt == 4:
    print("You have selected multiplication")
    input1 = int(input("Enter your first integer: "))
    input2 = int(input("Enter your second integer: "))
    print("\nThe multiplication of",input1,"and",input2,"is",(input1*input2))

if initialPrompt == 5:
    print("You have selected modulus")
    input1 = int(input("Enter your first integer: "))
    input2 = int(input("Enter your second integer: "))
    print("\nThe modulus of",input1,"and",input2,"is",(input1%input2))
    