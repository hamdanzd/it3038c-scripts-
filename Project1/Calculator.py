#This Python script is a basic text-based calculator that allows users to perform addition, subtraction, multiplication, and division.
#How to use: select an operation and input two numbers for the calculation. The script will display the result.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Welcome to my calculator!")

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        print("Thanks for using my calculator. Goodbye!")
        break

    if user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "add":
            print(f"The result is: {add(num1, num2)}")
        elif user_input == "subtract":
            print(f"The result is: {subtract(num1, num2)}")
        elif user_input == "multiply":
            print(f"The result is: {multiply(num1, num2)}")
        elif user_input == "divide":
            result = divide(num1, num2)
            if result == "Cannot divide by zero":
                print(result)
            else:
                print(f"The result is: {result}")
    else:
        print("Invalid input. Please try again.")

