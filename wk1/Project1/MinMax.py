# MinMax.py
""" Compares 5 integer values to determine the minimum and maximum"""

# welcome prompt
print("Welcome to the Python MinMax Application!")
print("This application calculates the minimum and maximum of 5 integer values\
 entered by a user.")

# int() converts input's string to int
input1 = int(input("Enter your first integer: "))
input2 = int(input("Enter your second integer: "))
input3 = int(input("Enter your third integer: "))
input4 = int(input("Enter your fourth integer: "))
input5 = int(input("Enter your fifth integer: "))

#built in min() and max() to avoid excessive conditionals 
print()
minimum = min(input1, input2, input3, input4, input5)
print("The minimum integer was",minimum)
maximum = max(input1, input2, input3, input4, input5)
print("The maximum integer was",maximum)