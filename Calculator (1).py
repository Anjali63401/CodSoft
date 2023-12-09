#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    return num1 / num2

# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Enter your choice (1-4): "))

# Perform the calculation based on the chosen operation
if operation == 1:
    result = add(num1, num2)
    operator = "+"
elif operation == 2:
    result = subtract(num1, num2)
    operator = "-"
elif operation == 3:
    result = multiply(num1, num2)
    operator = "*"
elif operation == 4:
    result = divide(num1, num2)
    operator = "/"
else:
    print("Invalid choice!")

# Display the result
print(f"\n{num1} {operator} {num2} = {result}")


# In[ ]:




