def calculate_and_store(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Invalid")
            return
    elif operator == '^':
        result = num1 ** num2
    elif operator == '%':
        result = num1 % num2
    return result


while True:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid")
        break

    operator = input("Enter the operator (+, -, *, /, ^, %): ")
    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^" or operator == "%":
        pass
    else:
        print("Invalid")
        break

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid")
        break

    result = calculate_and_store(num1, num2, operator)
    break

print(result)
