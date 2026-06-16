def add(num1, num2):
        return num1 + num2
    
def subtract(num1, num2):
        return num1 - num2
    
def multiply(num1, num2):
        return num1 * num2
    
def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            return None
        
def main():
    print("Welcome to the Alexandre's calculator!")
    print("Please enter the first number:")
    num1 = float(input())
    print("Please enter the second number:")
    num2 = float(input())
    print("Please enter the operation (+, -, *, /):")
    operation = input()
    
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Error: Invalid operation.")
        return
    
    print(f"The result is: {result}")


main()