import sys
import time
def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)

logo = ''' 

  _   _       _____ _       _____        __     ___        ____  _     _ _   _       _     
 | \ | | __ _|  ___(_)___  |_   _|_ _ _ _\ \   / (_)_ __  / ___|| |__ (_) | | | __ _| |__  
 |  \| |/ _` | |_  | / __|   | |/ _` | '_ \ \ / /| | '__| \___ \| '_ \| | |_| |/ _` | '_ \ 
 | |\  | (_| |  _| | \__ \   | | (_| | | | \ V / | | |     ___) | | | | |  _  | (_| | |_) |
 |_| \_|\__,_|_|   |_|___/   |_|\__,_|_| |_|\_/  |_|_|    |____/|_| |_|_|_| |_|\__,_|_.__/ 
                                                                                                                                                                  

'''
animated(logo)


import math

def add(x, y):
  """Adds two numbers"""
  return x + y

def subtract(x, y):
  """Subtracts two numbers"""
  return x - y

def multiply(x, y):
  """Multiplies two numbers"""
  return x * y

def divide(x, y):
  """Divides two numbers, handling division by zero"""
  if y == 0:
    return "Error: Cannot divide by zero"
  else:
    return x / y

def power(x, y):
  """Calculates x raised to the power of y"""
  return x**y

def factorial(n):
  """Calculates the factorial of a non-negative integer"""
  if n < 0:
    return "Error: Factorial is not defined for negative numbers"
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n+1):
      result *= i
    return result

def sine(x):
  """Calculates the sine of an angle in radians"""
  return math.sin(x)

def cosine(x):
  """Calculates the cosine of an angle in radians"""
  return math.cos(x)

def tangent(x):
  """Calculates the tangent of an angle in radians, handling division by zero"""
  if math.cos(x) == 0:
    return "Error: Cannot calculate tangent at 90 degrees (+/- n * 180)"
  else:
    return math.tan(x)

def absolute_value(x):
  """Calculates the absolute value of a number"""
  return abs(x)

def logarithm(x, base):
  """Calculates the logarithm of x to base (default base 10)"""
  if x <= 0:
    return "Error: Logarithm is not defined for non-positive numbers"
  else:
    return math.log(x, base)  # Base argument is optional

def calculate(num1, operator, num2):
  """Performs the chosen operation based on operator"""
  try:
    if operator == "+":
      return add(num1, num2)
    elif operator == "-":
      return subtract(num1, num2)
    elif operator == "*":
      return multiply(num1, num2)
    elif operator == "/":
      return divide(num1, num2)
    elif operator == "^":
      return power(num1, num2)
    elif operator == "!":
      return factorial(num2)  # Factorial applied to second number
    elif operator == "sin":
      return sine(num2)  # Trigonometric functions use radians
    elif operator == "cos":
      return cosine(num2)
    elif operator == "tan":
      return tangent(num2)
    elif operator == "abs":
      return absolute_value(num2)  # Absolute value applied to second number
    elif operator == "log":
      return logarithm(num2, base=10)  # Default base 10 for logarithms
    else:
      return "Invalid operator"
  except ValueError:
    return "Error: Invalid input"

while True:
  # Get user input
  num1 = float(input("Enter first number: "))
  operator = input("Enter operator (+, -, *, /, ^, !, sin, cos, tan, abs, log): ")
  num2 = float(input("Enter second number: "))

  # Perform calculation and handle errors
  result = calculate(num1, operator, num2)

  # Display result
  print("Result:", result)

  # Ask user if they want to continue
  choice = input("Do you want to continue? (y/n): ")
  if choice.lower() != "y":
    break

print("Calculator ending...")
