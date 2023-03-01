from art import logo

def add(n1, n2):
    return  (n1 + n2)

def subtract(n1, n2):
    return (n1 - n2)

def multiply(n1, n2):
    return (n1 * n2)

def divide(n1, n2):
    return (n1 / n2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# num1 = int(input("What's the first number? "))
# for operation in operations: print(operation)
# symbol_operation = input("Pick an operation from the line above: ")
# num2 = int(input("What's the second number? "))
# calculation_function = operations[symbol_operation]
# # calculation_function = operations[symbol_operation]
# # calculation_function = add
# #answer = calculation_function(num1, num2) = add(num1, num2)
# first_answer = calculation_function(num1, num2)
# print(f"{num1} {symbol_operation} {num2} = {first_answer}")

# "Type 'y' to continue calculating with {valor}, or type 'n' to exit:"

# symbol_operation = input("Pick an another operation: ")
# calculation_function = operations[symbol_operation]
# num3 = int(input("What's the next number? "))
# second_answer = calculation_function(first_answer, num3)
# print(f"{first_answer} {symbol_operation} {num3} = {second_answer}")

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number? "))
    for operation in operations: print(operation)
    
    while True:
        symbol_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[symbol_operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {symbol_operation} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ") == "y":
            num1 = answer
            continue
        else:
            calculator()
            break
            
calculator()