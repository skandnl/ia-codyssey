def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def evaluate_expression(expression):
    try:
        parts = expression.strip().split()
        if len(parts) != 3:
            return "Invalid input format. Use: number operator number"

        a_str, operator, b_str = parts
        a = float(a_str)
        b = float(b_str)

        if operator == '+':
            return add(a, b)
        elif operator == '-':
            return subtract(a, b)
        elif operator == '*':
            return multiply(a, b)
        elif operator == '/':
            return divide(a, b)
        else:
            return "Invalid operator."

    except ValueError:
        return "Invalid number format."

if __name__ == "__main__":
    mode = input("Select mode (1: manual input, 2: expression input): ")

    if mode == "1":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == "+":
                result = add(a, b)
            elif operator == "-":
                result = subtract(a, b)
            elif operator == "*":
                result = multiply(a, b)
            elif operator == "/":
                result = divide(a, b)
            else:
                result = "Invalid operator."
        except ValueError:
            result = "Invalid input. Please enter numbers."

        print(f"Result: {result}")

    elif mode == "2":
        expression = input("Enter expression (e.g., 2 + 3): ")
        result = evaluate_expression(expression)
        print(f"Result: {result}")

    else: