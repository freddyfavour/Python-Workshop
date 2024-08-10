first_value = int(input("Enter the first number: "))
second_value = int(input("Enter the second number: "))
symbol = input("Enter the symbol + - / or *: ")

def multiply(a, b):
  print(f"{a} multiplied by {b} gives {a * b}")

def divide(a, b):
  print(f"{a} divided by {b} gives {a / b}")

def subtract(a, b):
  print(f"{a} minus {b} gives {a - b}")

def add(a, b):
  print(f"{a} added to {b} gives {a + b}")

if symbol == "*":
  multiply(first_value,second_value)

if symbol == "/":
  divide(first_value,second_value)

if symbol == "+":
  add(first_value,second_value)

if symbol == "-":
  subtract(first_value,second_value)